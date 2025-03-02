install.packages("tm")
install.packages("slam")

library(tm)
library(slam)

# Define the corpus
corpus <- c(
  "this is the first document",
  "and this is the second document",
  "also have the third document",
  "this is the fourth document"
)

# Create a text corpus
docs <- Corpus(VectorSource(corpus))

# Convert to Document-Term Matrix (DTM)
dtm <- DocumentTermMatrix(docs, control = list(wordLengths = c(1, Inf)))

# Convert DTM to a data frame
df <- as.data.frame(as.matrix(dtm))
colnames(df) <- colnames(as.matrix(dtm))

# Print the term-document matrix
print(df)

# Rows where 'this' AND 'first' are present
AllAND <- df[df$this == 1 & df$first == 1, ]
print(paste("Indices where 'this' AND 'first' present:", rownames(AllAND)))

# Rows where 'this' OR 'first' are present
AllOR <- df[df$this == 1 | df$first == 1, ]
print(paste("Indices where 'this' OR 'first' present:", rownames(AllOR)))

# Rows where 'and' is NOT present
ALLnot <- df[df$and == 0, ]
print(paste("Indices where 'and' is NOT present:", rownames(ALLnot)))
