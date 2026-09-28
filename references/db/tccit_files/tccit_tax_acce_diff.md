# 折旧摊销税会差异台账-tccit_tax_acce_diff

## 折旧摊销税会差异台账-主表 t_tdm_totalassets_mes

- **表名称：** 折旧摊销税会差异台账-主表
- **表名：** t_tdm_totalassets_mes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswjsdqzjtxe | 税务实际当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际当期折旧摊销额 |
| 3 | fcleaningdate | 清理日期 | timestamp | 0 |  |  | null | 清理日期 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fjszjtxlx | 加速折旧摊销类型 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 6 | fremarks | fremarks | varchar | 255 |  | √ | ' ' |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fassetdataid | 资产编码 | int8 | 64 |  | √ | 0 | 资产清单 tdm_asset_data |
| 9 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 10 | fkjljzjtxe | 会计累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计累计折旧摊销额 |
| 11 | fdeclarethisperiod | 本期是否应申报 | bpchar | 1 |  | √ | ' ' | 本期是否应申报 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fswjsljzjtxe | 税务实际累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际累计折旧摊销额 |
| 14 | fljjszjyswzjcy | 累计实际折旧与税务一般折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 累计实际折旧与税务一般折旧差异 |
| 15 | fassetsvalue | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 16 | fswjszjtxff | 税务实际折旧摊销方法 | varchar | 50 |  | √ | ' ' | 税务实际折旧摊销方法 |
| 17 | fswjsbnzjtxe | 税务实际本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际本年折旧摊销额 |
| 18 | fswzclb | 税务资产类别 | varchar | 50 |  | √ | ' ' | 税务资产类别 |
| 19 | factperiods | factperiods | int8 | 64 |  | √ | 0 |  |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: on :在用 stop :停用 clean :清理 |
| 22 | fnstz | 纳税调整 | numeric | 23 | 10 | √ | 0 | 纳税调整 |
| 23 | fkjyjjcz | 会计预计净残值 | numeric | 23 | 10 | √ | 0.0000000000 | 会计预计净残值 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fkjzjtxqs | 会计折旧摊销期数 | int8 | 64 |  | √ | 0 | 会计折旧摊销期数 |
| 26 | fzcstatus | fzcstatus | varchar | 50 |  | √ | ' ' |  |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fbnjszjykjzjcy | 本年实际折旧与会计折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年实际折旧与会计折旧差异 |
| 29 | finitval | 初始资产原值 | numeric | 23 | 10 | √ | 0 | 初始资产原值 |
| 30 | fkjdqzjtxw | 会计当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计当期折旧摊销额 |
| 31 | fljjszjykjzjcy | 累计实际折旧与会计折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 累计实际折旧与会计折旧差异 |
| 32 | fswyjjcz | 税务预计净残值 | numeric | 23 | 10 | √ | 0.0000000000 | 税务预计净残值 |
| 33 | fpostingdate | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 34 | fentryid | 父级单据标识 | int8 | 64 |  | √ | 0 | 父级单据标识 |
| 35 | fswybzjtxff | 税务一般折旧摊销方法 | varchar | 50 |  | √ | ' ' | 税务一般折旧摊销方法 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fdqjszjyswzjcy | 本期税务实际与税务一般折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期税务实际与税务一般折旧差异 |
| 38 | fbnjszjyswzjcy | 本年税务实际与税务一般折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年税务实际与税务一般折旧差异 |
| 39 | fcalctaxbase | 计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 计税基础 |
| 40 | fswybbnzjtxe | 税务一般本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般本年折旧摊销额 |
| 41 | fsource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: handadd :手工新增 system :系统生成 import :数据引入 |
| 42 | fswybdqzjtxe | 税务一般当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般当期折旧摊销额 |
| 43 | ftaxassetstype | 税务资产类别 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 44 | fswybzjtxqs | 税务一般折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务一般折旧摊销期数 |
| 45 | fassetsname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | fzjtxmethod | 会计折旧摊销方法 | varchar | 50 |  | √ | ' ' | 会计折旧摊销方法 |
| 48 | fkjbnzjtxe | 会计本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计本年折旧摊销额 |
| 49 | fzctype | 资产类别 | varchar | 50 |  | √ | ' ' | 资产类别 |
| 50 | fswybljzjtxe | 税务一般累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般累计折旧摊销额 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | fdqjszjykjzjcy | 当期实际折旧与会计一般折旧差异 | numeric | 23 | 10 | √ | 0.0000000000 | 当期实际折旧与会计一般折旧差异 |
| 54 | frdaddition | 是否研发形成 | varchar | 50 |  | √ | ' ' | 是否研发形成,枚举: 1 :是 0 :否 |
| 55 | fswjszjtxqs | 税务实际折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务实际折旧摊销期数 |
| 56 | facceleratedepretype | 加速折旧类别 | varchar | 50 |  | √ | ' ' | 加速折旧类别 |
| 57 | fassetuse | 资产用途 | varchar | 50 |  | √ | ' ' | 资产用途,枚举: au_0 :用于研发投入 au_1 :用于高新投入 |
| 58 | fassetsnumber | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
| 59 | fdeclareperiod | 申报取值会计期间 | timestamp | 0 |  |  | null | 申报取值会计期间 |

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

## 折旧摊销税会差异台账-分表 t_tdm_totalassets_mes_a

- **表名称：** 折旧摊销税会差异台账-分表
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
