# 申报表修改历史-tctb_declare_his

## 申报表修改历史-主表 t_tctb_declare_his

- **表名称：** 申报表修改历史-主表
- **表名：** t_tctb_declare_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 修改原因 | varchar | 255 |  | √ | ' ' | 修改原因 |
| 3 | foriginalvalue | 修改前 | varchar | 2000 |  | √ | ' ' | 修改前 |
| 4 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 6 | fmodifytype | 修改类型 | varchar | 30 |  | √ | ' ' | 修改类型,枚举: 1 :系统变更 2 :修改变更 |
| 7 | ftargetvalue | 修改后 | varchar | 2000 |  | √ | ' ' | 修改后 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fcellid | 单元格id | varchar | 100 |  | √ | ' ' | 单元格id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_declare_his_ssid |  | fcellid,fsbbid |
| 2 | t_tctb_declare_his_pkey |  | fid |
