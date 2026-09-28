# 考勤同步出差申请单表(通用)-er_syntripreq

## 考勤同步出差申请单表(通用)-主表 t_er_syntripreq

- **表名称：** 考勤同步出差申请单表(通用)-主表
- **表名：** t_er_syntripreq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynstate | 同步状态 | varchar | 10 |  | √ | ' ' | 同步状态,枚举: 未同步 :no 已同步 :yes 同步失败 :fail |
| 3 | ftravelerid | 出差人ID | varchar | 80 |  | √ | ' ' | 出差人ID |
| 4 | ffailmessage | 失败信息 | varchar | 2000 |  |  | ' ' | 失败信息 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foptype | 操作类型 | varchar | 20 |  | √ | ' ' | 操作类型,枚举: create :create delete :delete |
| 7 | ftargetsystem | 目标系统 | varchar | 50 |  | √ | ' ' | 目标系统 |
| 8 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 9 | fdatano | 数据编号 | varchar | 80 |  | √ | ' ' | 数据编号 |
| 10 | fentryid | 行程明细表id | varchar | 2000 |  |  | ' ' | 行程明细表id |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_syntripreq |  | fid |
| 2 | idx_er_syntripreq_fbillno |  | fbillno |
