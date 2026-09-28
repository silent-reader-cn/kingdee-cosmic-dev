# 汇缴资产折旧摊销台账-tccit_hjzczjtx_account

## 汇缴资产折旧摊销台账-主表 t_tccit_hjzczjtx_account

- **表名称：** 汇缴资产折旧摊销台账-主表
- **表名：** t_tccit_hjzczjtx_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fjszjtxlx | 加速折旧摊销类型 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 5 | fbuytime | 购入日期 | timestamp | 0 |  |  | null | 购入日期 |
| 6 | ftaxassetstype | 税务资产类别 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fassetsname | 资产名称 | varchar | 50 |  | √ | ' ' | 资产名称 |
| 12 | fpostingdate | 折旧起始日期 | timestamp | 0 |  |  | null | 折旧起始日期 |
| 13 | fyfxcdwxzc | 是否研发形成的无形资产 | bpchar | 1 |  | √ | ' ' | 是否研发形成的无形资产 |
| 14 | fenable | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 0 :禁用 1 :可用 |
| 15 | fassetsnumber | 资产编码 | varchar | 50 |  | √ | ' ' | 资产编码 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fglqtnstzsx | 关联其他纳税调整事项 | varchar | 50 |  | √ | ' ' | 关联其他纳税调整事项,枚举: syqzc :使用权资产 bzsrxcdzc :不征税收入形成的资产 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fzzctype | 会计资产类别 | varchar | 50 |  | √ | ' ' | 会计资产类别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_hjzczjtx_account_assenum |  | fassetsnumber |
| 2 | idx_tccit_hjzczjtx_account |  | fnumber |
| 3 | pk_tccit_hjzczjtx_account |  | fentryid |
| 4 | idx_hjzczjtx_account_forgid |  | forgid |

---

## 资产折旧摊销明细-子表 t_tdm_totalassets_mes

- **表名称：** 资产折旧摊销明细-子表
- **表名：** t_tdm_totalassets_mes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswjsdqzjtxe | fswjsdqzjtxe | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fcleaningdate | fcleaningdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fjszjtxlx | fjszjtxlx | int8 | 64 |  | √ | 0 |  |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fassetdataid | fassetdataid | int8 | 64 |  | √ | 0 |  |
| 9 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 10 | fkjljzjtxe | 会计累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计累计折旧摊销额 |
| 11 | fdeclarethisperiod | fdeclarethisperiod | bpchar | 1 |  | √ | ' ' |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fswjsljzjtxe | 税务实际累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际累计折旧摊销额 |
| 14 | fljjszjyswzjcy | fljjszjyswzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fassetsvalue | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 16 | fswjszjtxff | fswjszjtxff | varchar | 50 |  | √ | ' ' |  |
| 17 | fswjsbnzjtxe | 税务实际本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际本年折旧摊销额 |
| 18 | fswzclb | fswzclb | varchar | 50 |  | √ | ' ' |  |
| 19 | factperiods | factperiods | int8 | 64 |  | √ | 0 |  |
| 20 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 21 | fassetstatus | fassetstatus | varchar | 50 |  | √ | ' ' |  |
| 22 | fnstz | fnstz | numeric | 23 | 10 | √ | 0 |  |
| 23 | fkjyjjcz | fkjyjjcz | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 25 | fkjzjtxqs | fkjzjtxqs | int8 | 64 |  | √ | 0 |  |
| 26 | fzcstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: on :在用 stop :停用 clean :清理 |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fbnjszjykjzjcy | fbnjszjykjzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | finitval | finitval | numeric | 23 | 10 | √ | 0 |  |
| 30 | fkjdqzjtxw | fkjdqzjtxw | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | fljjszjykjzjcy | fljjszjykjzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fswyjjcz | fswyjjcz | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fpostingdate | fpostingdate | timestamp | 0 |  |  | null |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fswybzjtxff | fswybzjtxff | varchar | 50 |  | √ | ' ' |  |
| 36 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 37 | fdqjszjyswzjcy | fdqjszjyswzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | fbnjszjyswzjcy | 本年实际折旧与税务一般折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年实际折旧与税务一般折旧差异 |
| 39 | fcalctaxbase | 计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 计税基础 |
| 40 | fswybbnzjtxe | 税务一般本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般本年折旧摊销额 |
| 41 | fsource | fsource | varchar | 50 |  | √ | ' ' |  |
| 42 | fswybdqzjtxe | fswybdqzjtxe | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | ftaxassetstype | ftaxassetstype | int8 | 64 |  | √ | 0 |  |
| 44 | fswybzjtxqs | fswybzjtxqs | int8 | 64 |  | √ | 0 |  |
| 45 | fassetsname | fassetsname | varchar | 200 |  | √ | ' ' |  |
| 46 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 47 | fzjtxmethod | fzjtxmethod | varchar | 50 |  | √ | ' ' |  |
| 48 | fkjbnzjtxe | 会计本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计本年折旧摊销额 |
| 49 | fzctype | fzctype | varchar | 50 |  | √ | ' ' |  |
| 50 | fswybljzjtxe | 税务一般累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般累计折旧摊销额 |
| 51 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 52 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 53 | fdqjszjykjzjcy | fdqjszjykjzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | frdaddition | frdaddition | varchar | 50 |  | √ | ' ' |  |
| 55 | fswjszjtxqs | fswjszjtxqs | int8 | 64 |  | √ | 0 |  |
| 56 | facceleratedepretype | facceleratedepretype | varchar | 50 |  | √ | ' ' |  |
| 57 | fassetuse | fassetuse | varchar | 50 |  | √ | ' ' |  |
| 58 | fassetsnumber | fassetsnumber | varchar | 200 |  | √ | ' ' |  |
| 59 | fdeclareperiod | fdeclareperiod | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_tmes_orgperiod |  | forgid,faccountingperiod |
| 2 | idx_tdm_totalassets_mes |  | forgid,fassetsnumber,faccountingperiod |
| 3 | pk_tdm_totalassets_mes |  | fid |

---

## 资产折旧摊销明细-分表 t_tdm_totalassets_mes_a

- **表名称：** 资产折旧摊销明细-分表
- **表名：** t_tdm_totalassets_mes_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcleandate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 3 | fjszjqc | 加速折旧情况 | varchar | 50 |  | √ | ' ' | 加速折旧情况 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_totalassets_mes_a |  | fid |
| 2 | idx_tdm_totalassets_mes_a |  | fentryid |

---

## 汇缴资产折旧摊销台账-多语言表 t_tccit_hjzczjtx_account_l

- **表名称：** 汇缴资产折旧摊销台账-多语言表
- **表名：** t_tccit_hjzczjtx_account_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_hjzczjtx_account_l |  | fpkid |
| 2 | idx_tccit_hjzczjtx_account_l_0 |  | fentryid,flocaleid |
