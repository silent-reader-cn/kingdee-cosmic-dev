# 翻译工作台-tlmgt_wordunit

## 翻译工作台-主表 t_tlmgt_wordunit

- **表名称：** 翻译工作台-主表
- **表名：** t_tlmgt_wordunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftrglang | 目标语言 | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 3 | fwordhash | 词条长标识 | varchar | 32 |  | √ | ' ' | 词条长标识 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsrcdir | 源文内容方向 | varchar | 32 |  | √ | ' ' | 源文内容方向,枚举: auto :自动 ltr :从左至右 rtl :从右至左 |
| 6 | ftranslaterid | 翻译人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbillstatus | 单据状态 | varchar | 32 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fsource | 源文 | varchar | 1024 |  | √ | ' ' | 源文 |
| 11 | ftarget | 译文 | varchar | 1024 |  | √ | ' ' | 译文 |
| 12 | ftrgdir | 译文内容方向 | varchar | 32 |  | √ | ' ' | 译文内容方向,枚举: auto :自动 ltr :从左至右 rtl :从右至左 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fwordkey | 词条标识 | varchar | 500 |  | √ | ' ' | 词条标识 |
| 16 | ftranslatetime | 翻译时间 | timestamp | 0 |  |  | null | 翻译时间 |
| 17 | ftranslatestate | 译文翻译状态 | varchar | 32 |  | √ | ' ' | 译文翻译状态,枚举: INITIAL :待翻译 TRANSLATED :已翻译 |
| 18 | fbillno | 系统唯一标识 | varchar | 64 |  | √ | ' ' | 系统唯一标识 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fsrclang | 源语言 | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 21 | ftransfile | 翻译文件 | int8 | 64 |  | √ | 0 | [翻译文件 tlmgt_transfile](../tlmgt_files/tlmgt_transfile.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_wordfile |  | ftransfile |
| 2 | idx_t_tlmgt_word |  | fbillno |
| 3 | pk_t_tlmgt_wordunit |  | fid |
| 4 | idx_t_tlmgt_word_src |  | fsrclang,ftrglang,ftransfile |
