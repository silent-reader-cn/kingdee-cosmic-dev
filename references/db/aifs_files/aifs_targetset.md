# 指标-aifs_targetset

## 核算维度-多选基础资料表 t_aifs_asstacttype

- **表名称：** 核算维度-多选基础资料表
- **表名：** t_aifs_asstacttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aifs_asstacttype_pkey |  | fpkid |
| 2 | idx_aifs_asstacttype |  | fid |

---

## 指标-多语言表 t_aifs_targetset_l

- **表名称：** 指标-多语言表
- **表名：** t_aifs_targetset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aifs_targetset_l |  | fid,flocaleid |
| 2 | t_aifs_targetset_l_pkey |  | fpkid |

---

## 指标-主表 t_aifs_targetset

- **表名称：** 指标-主表
- **表名：** t_aifs_targetset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbroadcaststlye | fbroadcaststlye | bpchar | 1 |  | √ | ' ' |  |
| 3 | fuserdefined5id | fuserdefined5id | int8 | 64 |  | √ | 0 |  |
| 4 | fuserdefined6id | fuserdefined6id | int8 | 64 |  | √ | 0 |  |
| 5 | faccrual | faccrual | bpchar | 1 |  | √ | ' ' |  |
| 6 | faccountfieldid | faccountfieldid | int8 | 64 |  | √ | 0 |  |
| 7 | fmodelid | fmodelid | int8 | 64 |  | √ | 0 |  |
| 8 | fscenarioid | fscenarioid | int8 | 64 |  | √ | 0 |  |
| 9 | fuserdefined2id | fuserdefined2id | int8 | 64 |  | √ | 0 |  |
| 10 | fuserdefined3id | fuserdefined3id | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatedatefield | fcreatedatefield | timestamp | 0 |  |  | null |  |
| 12 | fuserdefined4id | fuserdefined4id | int8 | 64 |  | √ | 0 |  |
| 13 | freportaccrualid | freportaccrualid | int8 | 64 |  | √ | 0 |  |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fuserdefined1id | fuserdefined1id | int8 | 64 |  | √ | 0 |  |
| 16 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 19 | finternalcompanyid | finternalcompanyid | int8 | 64 |  | √ | 0 |  |
| 20 | fcurrencyfieldid | fcurrencyfieldid | int8 | 64 |  | √ | 0 |  |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 22 | fmultigaapid | fmultigaapid | int8 | 64 |  | √ | 0 |  |
| 23 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 24 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 25 | fprocessid | fprocessid | int8 | 64 |  | √ | 0 |  |
| 26 | freportbalanceid | freportbalanceid | int8 | 64 |  | √ | 0 |  |
| 27 | faccounttableid | faccounttableid | int8 | 64 |  | √ | 0 |  |
| 28 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 29 | fbalance | fbalance | bpchar | 1 |  | √ | ' ' |  |
| 30 | fenable | fenable | bpchar | 1 |  | √ | ' ' |  |
| 31 | faudittrailid | faudittrailid | int8 | 64 |  | √ | 0 |  |
| 32 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 33 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 34 | fnumbersource | fnumbersource | bpchar | 1 |  | √ | ' ' |  |
| 35 | faccountid | faccountid | int8 | 64 |  | √ | 0 |  |
| 36 | fratiotype | fratiotype | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aifs_targetset |  | fnumber |
| 2 | t_aifs_targetset_pkey |  | fid |
