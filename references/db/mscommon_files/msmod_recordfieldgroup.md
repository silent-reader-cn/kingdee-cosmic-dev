# 核销记录分组-msmod_recordfieldgroup

## 核销记录分组-主表 t_msmod_recordfieldgroup

- **表名称：** 核销记录分组-主表
- **表名：** t_msmod_recordfieldgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 2 :禁用 1 :可用 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 核销单据类型 msmod_billtype |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fwftype | 核销类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 9 | fgroupfield | 分组字段 | varchar | 255 |  | √ | ' ' | 分组字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_recordfieldgroup |  | fid |
| 2 | idx_recordfieldgroup_type |  | fwftype |
