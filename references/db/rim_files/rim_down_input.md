# 进项发票下载临时表-rim_down_input

## 进项发票下载临时表-主表 t_rim_down_input

- **表名称：** 进项发票下载临时表-主表
- **表名：** t_rim_down_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffpy_serial_no | 发票云发票流水号 | varchar | 36 |  | √ | ' ' | 发票云发票流水号 |
| 3 | fsync_status | 同步状态 | varchar | 2 |  | √ | ' ' | 同步状态,枚举: 1 :已同步 2 :未同步 0 :同步失败 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | finvoice_json | json数据 | varchar | 255 |  | √ | ' ' | json数据 |
| 6 | finout | 进销项 | varchar | 2 |  | √ | ' ' | 进销项,枚举: 1 :进项 2 :销项 |
| 7 | fhandle_num | 处理次数 | int4 | 32 |  | √ | 0 | 处理次数 |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fserial_no | 流水号 | varchar | 36 |  | √ | ' ' | 流水号 |
| 11 | fdata_type | 数据类型 | varchar | 2 |  | √ | ' ' | 数据类型,枚举: 1 :进项表头数据 2 :缺抵扣信息的进项数据 3 :进项完整数据 |
| 12 | finvoice_json_tag | json数据_详情 | text | 0 |  |  | null | json数据_详情 |
| 13 | ferror_code | 错误代码 | varchar | 10 |  | √ | ' ' | 错误代码 |
| 14 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_down_input2 |  | fsync_status |
| 2 | idx_rim_down_input |  | fserial_no |
| 3 | idx_rim_down_input_time |  | fmodifytime |
| 4 | pk_rim_down_input |  | fid |
