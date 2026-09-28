# 费用项目-er_expenseitemedit

## 费用项目-多语言表 t_er_expenseitem_l

- **表名称：** 费用项目-多语言表
- **表名：** t_er_expenseitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 7 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_expenseitem_l_pkey |  | fpkid |
| 2 | idx_er_eil_fid |  | fid,flocaleid |

---

## 费用项目-使用范围位图表 t_er_expenseitem_m

- **表名称：** 费用项目-使用范围位图表
- **表名：** t_er_expenseitem_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_expenseitem_m |  | forgid |

---

## 费用项目-使用范围表 t_er_expenseitem_u

- **表名称：** 费用项目-使用范围表
- **表名：** t_er_expenseitem_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_expenseitem_u_uo |  | fuseorgid |
| 2 | t_er_expenseitem_u_pkey |  | fdataid,fuseorgid |

---

## 费用项目-主表 t_er_expenseitem

- **表名称：** 费用项目-主表
- **表名：** t_er_expenseitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | foffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fpiccoclor | fpiccoclor | varchar | 100 |  | √ | ' ' |  |
| 10 | fisvactax | 价税分离 | bpchar | 1 |  | √ | '0' | 价税分离 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | freimbdisc | 报销事由 | varchar | 255 |  |  | null | 报销事由 |
| 13 | fstatus | 数据状态 | varchar | 25 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fpic | fpic | varchar | 100 |  | √ | ' ' |  |
| 17 | freimburseamountctlmethod | 额度控制方法 | bpchar | 1 |  | √ | 'A' | 额度控制方法,枚举: A :累计控制 B :按月控制 E :按季控制 C :按年控制 |
| 18 | freimctltype | 控制类型 | bpchar | 1 |  | √ | '1' | 控制类型,枚举: 1 :定额控制 2 :混合控制 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fpicurl | fpicurl | varchar | 255 |  | √ | ' ' |  |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 26 | fcomment | 备注(废弃) | varchar | 255 |  | √ | ' ' | 备注(废弃) |
| 27 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 28 | fisshowinmob | 移动端显示 | bpchar | 1 |  | √ | '0' | 移动端显示 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 31 | flongnumber | 长编码 | varchar | 100 |  | √ | ' ' | 长编码 |
| 32 | freimburseamountctlcount | 额度控制次数 | int4 | 32 |  | √ | 0 | 额度控制次数 |
| 33 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 34 | fmigsrc | fmigsrc | int4 | 32 |  | √ | 0 |  |
| 35 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 36 | fiscommon | 常用 | bpchar | 1 |  | √ | '0' | 常用 |
| 37 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 38 | fisrelatedvehicle | 关联交通工具 | bpchar | 1 |  | √ | '0' | 关联交通工具 |
| 39 | fexpenseitemicon | 选择图标 | varchar | 255 |  | √ | ' ' | 选择图标 |
| 40 | fhaverelorg | 是否关联部门 | bpchar | 1 |  | √ | '0' | 是否关联部门 |
| 41 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 42 | fisreimburseamountctl | 额度控制 | bpchar | 1 |  | √ | '0' | 额度控制,枚举: 0 :无控制 1 :员工额度控制 2 :部门额度控制 3 :费用标准控制 |
| 43 | frelbilltype | 关联单据 | varchar | 620 |  | √ | ' ' | 关联单据 |
| 44 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 45 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 46 | fisdefault | 默认预置（新增单据时） | bpchar | 1 |  | √ | '0' | 默认预置（新增单据时） |
| 47 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_expenseitem_master |  | fmasterid |
| 2 | idx_t_er_expenseitem_createorg |  | fcreateorgid |
| 3 | t_er_expenseitem_pkey |  | fid |
| 4 | ix_er_expenseitem_parentid |  | fparentid |
| 5 | idx_er_exit_fnumber |  | fnumber |
