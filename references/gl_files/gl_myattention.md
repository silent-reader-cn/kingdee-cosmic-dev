# 我关注的科目配置-gl_myattention

## 我关注的科目配置-主表 t_gl_myattention

- **表名称：** 我关注的科目配置-主表
- **表名：** t_gl_myattention

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: beginlocal :期初余额 debitlocal :本期借方发生 creditlocal :本期贷方发生 endlocal :期末余额 yeardebitlocal :本年借方累计发生额 yearcreditlocal :本年贷方累计发生额 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | faccountid | faccountid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_myattention |  | fcreatorid |
| 2 | t_gl_myattention_pkey |  | fid |

---

## 科目-多选基础资料表 t_gl_myattentionaccount

- **表名称：** 科目-多选基础资料表
- **表名：** t_gl_myattentionaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_myattentionaccount_pkey |  | fpkid |
| 2 | idx_gl_myattentionaccount |  | fid |
