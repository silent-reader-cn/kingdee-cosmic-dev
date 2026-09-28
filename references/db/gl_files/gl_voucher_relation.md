# 凭证折算关系-gl_voucher_relation

## 凭证折算关系-主表 t_gl_relation

- **表名称：** 凭证折算关系-主表
- **表名：** t_gl_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fsrcvoucherid | 来源凭证ID | int8 | 64 |  | √ | 0 | 来源凭证ID |
| 4 | fdestvoucherid | 目标凭证ID | int8 | 64 |  | √ | 0 | 目标凭证ID |
| 5 | fdestbookid | 目标账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 6 | fsrcbookid | 来源账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 7 | fruleid | 凭证折算规则ID | int8 | 64 |  | √ | 0 | 凭证折算规则ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_relation_fdestvch |  | fdestvoucherid |
| 2 | pk_t_gl_relation |  | fid |
