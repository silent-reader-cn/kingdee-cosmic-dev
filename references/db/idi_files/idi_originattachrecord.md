# 附件识别原始接口结果-idi_originattachrecord

## 附件识别原始接口结果-主表 t_idi_originattachrecord

- **表名称：** 附件识别原始接口结果-主表
- **表名：** t_idi_originattachrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillnumber | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 3 | fresult_tag | 识别结果_详情 | text | 0 |  |  | null | 识别结果_详情 |
| 4 | fcreaterfield_id | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | frequestno | 请求编号 | varchar | 80 |  | √ | ' ' | 请求编号 |
| 6 | fdatasource | 数据来源 | bpchar | 1 |  | √ | ' ' | 数据来源,枚举: 0 :AI 1 :令才 |
| 7 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fresult | 识别结果 | varchar | 255 |  |  | null | 识别结果 |
| 9 | fbillentity | 单据标识 | varchar | 80 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_originattachrecord |  | fid |
| 2 | idx_idi_originattachrecord_no |  | frequestno |
