# 议价报价截止时间变更-src_negotiate_timechg

## 议价报价截止时间变更-主表 t_src_negotiate_chg

- **表名称：** 议价报价截止时间变更-主表
- **表名：** t_src_negotiate_chg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 3 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 4 | fnegotiateid | 议价单号 | int8 | 64 |  | √ | 0 | 议价单F7 src_negotiatebillf7 |
| 5 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 6 | fnewstopbiddate | 报价截止时间(变更后) | timestamp | 0 |  |  | null | 报价截止时间(变更后) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_negotiate_chg |  | fid |
| 2 | idx_src_negotiate_chg_pid |  | fparentid |
