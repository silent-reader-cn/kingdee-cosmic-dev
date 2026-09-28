# 信用主题看板数据源-ssc_creditboarddata

## 信用扣分明细分录-多语言表 t_tk_creditboard_detail_l

- **表名称：** 信用扣分明细分录-多语言表
- **表名：** t_tk_creditboard_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbiztypename | 业务类型名称 | varchar | 100 |  | √ | ' ' | 业务类型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_creditboard_detail_l |  | fpkid |
| 2 | idx_ssc_creboadet_l_fenflocid |  | fentryid,flocaleid |

---

## 信用主题看板数据源-主表 t_tk_creditboarddata

- **表名称：** 信用主题看板数据源-主表
- **表名：** t_tk_creditboarddata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftaskcompletednum | 共享任务完成量 | int4 | 32 |  | √ | 0 | 共享任务完成量 |
| 4 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 5 | ftasksubscorenum | ftasksubscorenum | int4 | 32 |  | √ | 0 |  |
| 6 | fbizdate | 业务日期 | int4 | 32 |  | √ | 0 | 业务日期 |
| 7 | ftasksubscoredetail | ftasksubscoredetail | int4 | 32 |  | √ | 0 |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_creditboard_sscbizdate |  | fsscid,fbizdate |
| 2 | pk_t_tk_creditboarddata |  | fid |

---

## 信用扣分明细分录-子表 t_tk_creditboard_detail

- **表名称：** 信用扣分明细分录-子表
- **表名：** t_tk_creditboard_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuser | 员工 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsubscoretype | 扣分类型 | bpchar | 1 |  | √ | '0' | 扣分类型,枚举: 0 :共享审核批退原因 1 :审批通过但有违规 2 :共享审核 3 :影像超期 4 :质检任务 |
| 6 | fbillbiztypeid | 业务类型id | varchar | 50 |  | √ | ' ' | 业务类型id |
| 7 | fbizsys | 业务系统 | int8 | 64 |  | √ | 0 | 业务系统 bas_extenderp |
| 8 | fbizbill | 单据实体 | varchar | 50 |  | √ | ' ' | 单据实体 |
| 9 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 10 | fsubscore | 信用扣分 | numeric | 19 | 6 | √ | 0.000000 | 信用扣分 |
| 11 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbiztypeentity | 业务类型实体 | varchar | 50 |  | √ | ' ' | 业务类型实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_creditboadet_fbizbill |  | fbizbill |
| 2 | pk_t_tk_creditboard_detail |  | fentryid |
| 3 | idx_ssc_creditboadet_fid |  | fid |
| 4 | idx_ssc_creditboadet_ftaskid |  | ftaskid |

---

## 信用主题看板数据源-多语言表 t_tk_creditboarddata_l

- **表名称：** 信用主题看板数据源-多语言表
- **表名：** t_tk_creditboarddata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_creditboarddata_l |  | fpkid |
| 2 | idx_ssc_creboadata_l_flocid |  | fid,flocaleid |
