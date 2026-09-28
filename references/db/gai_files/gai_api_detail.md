# API调用明细-gai_api_detail

## API调用明细-主表 t_gai_api_detail

- **表名称：** API调用明细-主表
- **表名：** t_gai_api_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  |  | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |
| 5 | ferrcode | 错误码 | varchar | 50 |  |  | ' ' | 错误码 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fchatsessionid | 会话ID | varchar | 100 |  |  | ' ' | 会话ID |
| 8 | fapiinfo | API | int8 | 64 |  | √ | 0 | [API基础信息 gai_api_info](../gai_files/gai_api_info.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 调用编码 | varchar | 30 |  | √ | ' ' | 调用编码 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcost | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_api_detail |  | fid |
