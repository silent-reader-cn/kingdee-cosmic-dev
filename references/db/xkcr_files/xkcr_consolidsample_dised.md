# 合并报表模板（分发后）-xkcr_consolidsample_dised

## 合并报表模板（分发后）-主表 t_xkrpt_rpt

- **表名称：** 合并报表模板（分发后）-主表
- **表名：** t_xkrpt_rpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [合并报表模板分组 xkcr_consolidationgroup](../xkcr_files/xkcr_consolidationgroup.md) |
| 2 | fwiserpt | fwiserpt | text | 0 |  |  | null |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fsourceid | fsourceid | varchar | 36 |  | √ | ' ' |  |
| 5 | fcurrunitid | fcurrunitid | int8 | 64 |  | √ | 0 |  |
| 6 | fdocumentstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisautocreate | fisautocreate | bpchar | 1 |  | √ | '0' |  |
| 9 | fverifyresult | fverifyresult | varchar | 255 |  | √ | ' ' |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frptstyletype | frptstyletype | varchar | 10 |  | √ | ' ' |  |
| 13 | fday | fday | timestamp | 0 |  |  | null |  |
| 14 | ftranssourceid | ftranssourceid | varchar | 36 |  | √ | ' ' |  |
| 15 | fforbidderid | fforbidderid | int8 | 64 |  | √ | 0 |  |
| 16 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 17 | fverifydate | fverifydate | timestamp | 0 |  |  | null |  |
| 18 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 19 | frptstyle | frptstyle | text | 0 |  |  | null |  |
| 20 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 21 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | frptid | frptid | varchar | 36 |  | √ | ' ' | id |
| 24 | facctsystemid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fissample | fissample | bpchar | 1 |  | √ | '0' |  |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | farchivestatus | farchivestatus | bpchar | 1 |  | √ | '0' |  |
| 29 | fisautoshare | fisautoshare | bpchar | 1 |  | √ | '0' |  |
| 30 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |
| 31 | fpolicyid | fpolicyid | int8 | 64 |  | √ | 0 |  |
| 32 | fkeyword | fkeyword | varchar | 255 |  | √ | ' ' |  |
| 33 | fsampleid | fsampleid | varchar | 36 |  | √ | ' ' |  |
| 34 | frptmodel | frptmodel | text | 0 |  |  | null |  |
| 35 | fyear | fyear | int8 | 64 |  | √ | 0 |  |
| 36 | fperiod | fperiod | int8 | 64 |  | √ | 0 |  |
| 37 | fcreatestyle | fcreatestyle | varchar | 10 |  | √ | ' ' |  |
| 38 | fismain | fismain | bpchar | 1 |  | √ | '0' |  |
| 39 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 41 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 42 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 43 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 13 :工作底稿模板 10 :个别报表模板 31 :抵销表 30 :抵销表模板 2 :穿透报表 1 :报表 14 :汇总报表 17 :个别报表 20 :调整报表 3 :报表模板 4 :自定义报表 11 :合并报表模板 50 :阿米巴报表模板 16 :工作底稿 12 :汇总报表模板 15 :合并报表 |
| 44 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 45 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | [合并方案 xkcr_scopetype](../xkcr_files/xkcr_scopetype.md) |
| 46 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 47 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 48 | fverifystatus | fverifystatus | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | frptid | frptid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rpt |  | frptid |
| 2 | idx_xkrpt_rpt_fnumber |  | fnumber |

---

## 合并报表模板（分发后）-多语言表 t_xkrpt_rpt_l

- **表名称：** 合并报表模板（分发后）-多语言表
- **表名：** t_xkrpt_rpt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | frptid | frptid | varchar | 36 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rpt_l |  | fpkid |
| 2 | idx_xkrpt_rpt_l_frptid |  | frptid |
