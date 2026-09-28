# 附件识别解析后的结果记录-idi_processattachrecord

## 附件识别解析后的结果记录-主表 t_idi_processattachrecord

- **表名称：** 附件识别解析后的结果记录-主表
- **表名：** t_idi_processattachrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 4 | fprocessresult | 解析后的结果 | varchar | 255 |  |  | null | 解析后的结果 |
| 5 | fdatasource | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: 0 :AI 1 :令才 |
| 6 | fprocessresult_tag | 解析后的结果_详情 | text | 0 |  |  | null | 解析后的结果_详情 |
| 7 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffilemd5 | 文件MD5值 | varchar | 50 |  | √ | ' ' | 文件MD5值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_processrecord_md5 |  | ffilemd5 |
| 2 | pk_t_idi_processattachrecord |  | fid |
