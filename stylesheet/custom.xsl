<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:param name="column.count.body" select="2"/>
  <xsl:param name="column.count.back" select="2"/>
  <xsl:param name="chapter.autolabel" select="0"/>
  <xsl:param name="section.autolabel.max.depth" select="1"/>
  <xsl:param name="double.sided" select="1"/>

<xsl:attribute-set name="book.titlepage.recto.style">
  <xsl:attribute name="text-align">right</xsl:attribute>
  <xsl:attribute name="color">#00AFDC</xsl:attribute>
</xsl:attribute-set>

<xsl:param name="body.font.master">#00AFDC</xsl:param>

</xsl:stylesheet>



