# 项目余额-cas_projectbalance

## 项目余额-主表 t_cas_projectbalance

- **表名称：** 项目余额-主表
- **表名：** t_cas_projectbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyeardebitloc | 年借方金额本位币 | numeric | 23 | 10 | √ | 0 | 年借方金额本位币 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmonthcredit | 期贷方 | numeric | 23 | 10 | √ | 0 | 期贷方 |
| 6 | fyeardebit | 年借方 | numeric | 23 | 10 | √ | 0 | 年借方 |
| 7 | fyearcredit | 年贷方 | numeric | 23 | 10 | √ | 0 | 年贷方 |
| 8 | fyearbalance | 年末余额 | numeric | 23 | 10 | √ | 0 | 年末余额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fmonthbalance | 期末余额 | numeric | 23 | 10 | √ | 0 | 期末余额 |
| 15 | fyearcreditloc | 年贷方金额本位币 | numeric | 23 | 10 | √ | 0 | 年贷方金额本位币 |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fisbalanced | 是否结账 | bpchar | 1 |  | √ | '0' | 是否结账 |
| 18 | fyearstart | 年初余额 | numeric | 23 | 10 | √ | 0 | 年初余额 |
| 19 | fmonthdebit | 期借方 | numeric | 23 | 10 | √ | 0 | 期借方 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 23 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fmonthdebitloc | 期借方金额本位币 | numeric | 23 | 10 | √ | 0 | 期借方金额本位币 |
| 26 | fmonthcreditloc | 期贷方金额本位币 | numeric | 23 | 10 | √ | 0 | 期贷方金额本位币 |
| 27 | fmonthstart | 期初余额 | numeric | 23 | 10 | √ | 0 | 期初余额 |
| 28 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | fbasecurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fyearbalanceloc | 年末余额本位币 | numeric | 23 | 10 | √ | 0 | 年末余额本位币 |
| 31 | fyearstartloc | 年初余额本位币 | numeric | 23 | 10 | √ | 0 | 年初余额本位币 |
| 32 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fmonthbalanceloc | 期末余额本位币 | numeric | 23 | 10 | √ | 0 | 期末余额本位币 |
| 34 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 35 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 36 | fmonthstartloc | 期初余额本位币 | numeric | 23 | 10 | √ | 0 | 期初余额本位币 |
| 37 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_projectbalance |  | fid |
| 2 | idx_t_cas_projectbalance_master |  | fmasterid |
| 3 | ix_cas_projectbal_org |  | forgid |
| 4 | ix_cas_projectbal_pro |  | fproject |
| 5 | idx_t_cas_projectbalance_createorg |  | fcreateorgid |

---

## 项目余额-使用范围表 t_cas_projectbalance_u

- **表名称：** 项目余额-使用范围表
- **表名：** t_cas_projectbalance_u

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
| 1 | pk_t_cas_projectbalance_u |  | fdataid,fuseorgid |
| 2 | idx_t_cas_projectbalance_u_uo |  | fuseorgid |

---

## 项目余额-多语言表 t_cas_projectbalance_l

- **表名称：** 项目余额-多语言表
- **表名：** t_cas_projectbalance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  |  | null |  |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_projectbalance_l |  | fpkid |
| 2 | idx_cas_projtbal_l_fid |  | fid,flocaleid |
