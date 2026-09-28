# 账单池配置-er_bd_billingpoolcfg

## 账单池配置-多语言表 t_er_billpoolcfg_l

- **表名称：** 账单池配置-多语言表
- **表名：** t_er_billpoolcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 2000 |  |  | ' ' |  |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_billpoolcfg_l |  | fpkid |
| 2 | idx_billpoolcfg_fid |  | fid |

---

## 账单池配置-使用范围表 t_er_billpoolcfg_u

- **表名称：** 账单池配置-使用范围表
- **表名：** t_er_billpoolcfg_u

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
| 1 | pk_t_er_billpoolcfg_u |  | fdataid,fuseorgid |
| 2 | idx_t_er_billpoolcfg_u_uo |  | fuseorgid |

---

## 账单池配置-主表 t_er_billpoolcfg

- **表名称：** 账单池配置-主表
- **表名：** t_er_billpoolcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcanmanualadd | 允许手动录入账单 | bpchar | 1 |  | √ | '0' | 允许手动录入账单,枚举: 1 :是 0 :否 |
| 3 | fiscrossyear | 允许跨年 | bpchar | 1 |  | √ | '0' | 允许跨年,枚举: 1 :是 0 :否 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | funiquecon | 唯一性校验条件 | varchar | 40 |  | √ | ' ' | 唯一性校验条件,枚举: 1 :是 0 :否 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdupexpense | 重复报销 | varchar | 20 |  | √ | ' ' | 重复报销,枚举: STRICT_CONTROL :严格控制 TIP_CONTROL :仅提醒 NO_CONTROL :不控制 |
| 9 | fstatus | 数据状态 | varchar | 8 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcanimport | 允许导入账单 | bpchar | 1 |  | √ | '0' | 允许导入账单,枚举: 1 :是 0 :否 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fequalwl | 按往来单位过滤 | bpchar | 1 |  | √ | '0' | 按往来单位过滤,枚举: 1 :是 0 :否 |
| 16 | fenableoffset | 启用抵扣规则 | bpchar | 1 |  | √ | '0' | 启用抵扣规则,枚举: 1 :是 0 :否 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | frangofsync | 同步生成账单范围 | varchar | 30 |  | √ | ' ' | 同步生成账单范围,枚举: MutilAndManual :多次报销或手动新增发票 all :全部发票 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fctrlstrategy | 控制策略 | varchar | 20 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fcollectorselectrange | 收票人选择范围 | bpchar | 1 |  | √ | '1' | 收票人选择范围,枚举: 1 :本人 2 :本部门 3 :本公司 4 :全集团 |
| 24 | fctltype | 期限控制方式 | varchar | 20 |  | √ | ' ' | 期限控制方式,枚举: STRICT_CONTROL :严格控制 TIP_CONTROL :仅提醒 NO_CONTROL :不控制 |
| 25 | fperiod | 报销期限(天) | int4 | 32 |  | √ | 0 | 报销期限(天) |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fuptomonth | 第二年报销截止月份 | varchar | 8 |  | √ | ' ' | 第二年报销截止月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 28 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 29 | fequalcostcompany | 按费用承担公司过滤 | bpchar | 1 |  | √ | '0' | 按费用承担公司过滤,枚举: 1 :是 0 :否 |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_billpoolcfg_creater |  | fcreateorgid |
| 2 | idx_t_er_billpoolcfg_createorg |  | fcreateorgid |
| 3 | idx_t_er_billpoolcfg_master |  | fmasterid |
| 4 | pk_t_er_billpoolcfg |  | fid |
