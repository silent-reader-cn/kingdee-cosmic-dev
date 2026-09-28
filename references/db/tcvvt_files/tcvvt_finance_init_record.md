# 财务报表初始化记录表-tcvvt_finance_init_record

## 财务报表初始化记录表-主表 t_tcvvt_finance_init

- **表名称：** 财务报表初始化记录表-主表
- **表名：** t_tcvvt_finance_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 5 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 6 | fnsrtype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: FR0001 :一般企业会计准则（未执行） FR0002 :一般企业会计准则（已执行） FR0003 :小企业会计准则 FR0004 :企业会计制度 FR0011 :金融企业会计准则 |
| 7 | fisinit | 是否已初始化 | varchar | 50 |  | √ | ' ' | 是否已初始化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_financeinit_sbbid |  | fsbbid |
| 2 | pk_tcvvt_finance_init |  | fid |
