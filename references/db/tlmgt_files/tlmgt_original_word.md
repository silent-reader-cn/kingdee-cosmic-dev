# 抽取原始词条-tlmgt_original_word

## 抽取原始词条-主表 t_tlmgt_original_word

- **表名称：** 抽取原始词条-主表
- **表名：** t_tlmgt_original_word

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemtype | 元素类型 | varchar | 64 |  | √ | ' ' | 元素类型 |
| 3 | fstatus | 下推状态 | varchar | 64 |  | √ | ' ' | 下推状态,枚举: unpush :未下推 pushed :已下推 update :更新 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fwordkey | 词条标识 | varchar | 500 |  | √ | ' ' | 词条标识 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | flangtext_tag | 语言文本_详情 | text | 0 |  |  | null | 语言文本_详情 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flangtext | 语言文本 | varchar | 255 |  | √ | ' ' | 语言文本 |
| 10 | fschemeid | 抽取方案 | int8 | 64 |  | √ | 0 | [抽取方案 tlmgt_extract_scheme](../tlmgt_files/tlmgt_extract_scheme.md) |
| 11 | ffileid | 抽取原始文件 | int8 | 64 |  | √ | 0 | [抽取原始文件 tlmgt_original_file](../tlmgt_files/tlmgt_original_file.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_original_word |  | fid |
| 2 | idx_t_tlmgt_ori_fileid |  | ffileid |
| 3 | idx_t_tlmgt_ori_word |  | fwordkey,fstatus,ffileid |
