# 科目风险设置-gl_bill_accriskset

## 科目：-多选基础资料表 t_gl_accriskset_acc

- **表名称：** 科目：-多选基础资料表
- **表名：** t_gl_accriskset_acc

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
| 1 | t_gl_accriskset_acc_pkey |  | fpkid |
| 2 | idx_gl_accriskset_acc |  | fid |

---

## 科目风险设置-主表 t_gl_accriskset

- **表名称：** 科目风险设置-主表
- **表名：** t_gl_accriskset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 3 | fencodefilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 4 | faccedit | 科目编辑 | varchar | 30 |  | √ | ' ' | 科目编辑 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ffield | 字段 | varchar | 30 |  | √ | ' ' | 字段,枚举: debitlocal :借方发生额 creditlocal :贷方发生额 endlocal :余额 |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fsymbol | 条件 | varchar | 2 |  | √ | ' ' | 条件,枚举: = := <> :<> > :> >= :>= < :< <= :<= |
| 9 | faccounttableid | 科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 10 | fcurlocal | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 11 | fcurfor | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_accriskset_pkey |  | fid |
| 2 | idx_gl_accriskset |  | forgid,fuserid |
