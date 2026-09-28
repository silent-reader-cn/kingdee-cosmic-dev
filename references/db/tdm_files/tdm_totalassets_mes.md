# 资产折旧摊销信息-tdm_totalassets_mes

## 资产折旧摊销信息-主表 t_tdm_totalassets_mes

- **表名称：** 资产折旧摊销信息-主表
- **表名：** t_tdm_totalassets_mes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fswjsdqzjtxe | 税务实际当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际当期折旧摊销额 |
| 3 | fcleaningdate | fcleaningdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fjszjtxlx | fjszjtxlx | int8 | 64 |  | √ | 0 |  |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fassetdataid | fassetdataid | int8 | 64 |  | √ | 0 |  |
| 9 | faccountingperiod | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 10 | fkjljzjtxe | 会计累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计累计折旧摊销额 |
| 11 | fdeclarethisperiod | 本期是否应申报 | bpchar | 1 |  | √ | ' ' | 本期是否应申报 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fswjsljzjtxe | 税务实际累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际累计折旧摊销额 |
| 14 | fljjszjyswzjcy | fljjszjyswzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fassetsvalue | 资产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 资产原值 |
| 16 | fswjszjtxff | 税务实际折旧摊销方法 | varchar | 50 |  | √ | ' ' | 税务实际折旧摊销方法 |
| 17 | fswjsbnzjtxe | 税务实际本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务实际本年折旧摊销额 |
| 18 | fswzclb | fswzclb | varchar | 50 |  | √ | ' ' |  |
| 19 | factperiods | 实际已使用期数 | int8 | 64 |  | √ | 0 | 实际已使用期数 |
| 20 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 21 | fassetstatus | fassetstatus | varchar | 50 |  | √ | ' ' |  |
| 22 | fnstz | fnstz | numeric | 23 | 10 | √ | 0 |  |
| 23 | fkjyjjcz | 会计预计净残值 | numeric | 23 | 10 | √ | 0.0000000000 | 会计预计净残值 |
| 24 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 25 | fkjzjtxqs | 会计折旧摊销期数 | int8 | 64 |  | √ | 0 | 会计折旧摊销期数 |
| 26 | fzcstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: on :在用 stop :停用 clean :清理 |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fbnjszjykjzjcy | fbnjszjykjzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | finitval | finitval | numeric | 23 | 10 | √ | 0 |  |
| 30 | fkjdqzjtxw | 会计当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计当期折旧摊销额 |
| 31 | fljjszjykjzjcy | fljjszjykjzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fswyjjcz | 税务预计净残值 | numeric | 23 | 10 | √ | 0.0000000000 | 税务预计净残值 |
| 33 | fpostingdate | 折旧起始日期 | timestamp | 0 |  |  | null | 折旧起始日期 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fswybzjtxff | 税务一般折旧摊销方法 | varchar | 50 |  | √ | ' ' | 税务一般折旧摊销方法 |
| 36 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 37 | fdqjszjyswzjcy | fdqjszjyswzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | fbnjszjyswzjcy | fbnjszjyswzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fcalctaxbase | 计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 计税基础 |
| 40 | fswybbnzjtxe | 税务一般本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般本年折旧摊销额 |
| 41 | fsource | fsource | varchar | 50 |  | √ | ' ' |  |
| 42 | fswybdqzjtxe | 税务一般当期折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般当期折旧摊销额 |
| 43 | ftaxassetstype | 税务资产类别 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 44 | fswybzjtxqs | 税务一般折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务一般折旧摊销期数 |
| 45 | fassetsname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fzjtxmethod | 会计折旧摊销方法 | varchar | 50 |  | √ | ' ' | 会计折旧摊销方法 |
| 48 | fkjbnzjtxe | 会计本年折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 会计本年折旧摊销额 |
| 49 | fzctype | 会计资产类别 | varchar | 50 |  | √ | ' ' | 会计资产类别 |
| 50 | fswybljzjtxe | 税务一般累计折旧摊销额 | numeric | 23 | 10 | √ | 0.0000000000 | 税务一般累计折旧摊销额 |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 53 | fdqjszjykjzjcy | fdqjszjykjzjcy | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | frdaddition | frdaddition | varchar | 50 |  | √ | ' ' |  |
| 55 | fswjszjtxqs | 税务实际折旧摊销期数 | int8 | 64 |  | √ | 0 | 税务实际折旧摊销期数 |
| 56 | facceleratedepretype | facceleratedepretype | varchar | 50 |  | √ | ' ' |  |
| 57 | fassetuse | fassetuse | varchar | 50 |  | √ | ' ' |  |
| 58 | fassetsnumber | 资产编码 | varchar | 200 |  | √ | ' ' | 资产编码 |
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

## 资产折旧摊销信息-分表 t_tdm_totalassets_mes_a

- **表名称：** 资产折旧摊销信息-分表
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
