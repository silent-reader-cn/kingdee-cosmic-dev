# 用量概率计算日志-mds_probabilitylog

## 客舱构型-多选基础资料表 t_mds_probalog_cabin

- **表名称：** 客舱构型-多选基础资料表
- **表名：** t_mds_probalog_cabin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客舱构型 mpdm_cabinconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_cabin_id |  | fid |
| 2 | pk_mds_probalog_cabin |  | fpkid |

---

## 结果单据体-子表 t_mds_probabilityrp_log

- **表名称：** 结果单据体-子表
- **表名：** t_mds_probabilityrp_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | frpselectfilterval | 选择条件值(后台) | text | 0 |  |  | null | 选择条件值(后台) |
| 5 | frpselectfilter | 选择条件 | varchar | 2000 |  | √ | ' ' | 选择条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probarp_log_id |  | fid |
| 2 | pk_mds_probabilityrp_log |  | fentryid |

---

## 用量概率计算日志-多语言表 t_mds_probabilitylog_l

- **表名称：** 用量概率计算日志-多语言表
- **表名：** t_mds_probabilitylog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probabilitylog_l_fid |  | fid,flocaleid |
| 2 | pk_mds_probabilitylog_l |  | fpkid |

---

## 业务类型-多选基础资料表 t_mds_probalog_biztype

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_mds_probalog_biztype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probalog_biztype |  | fpkid |
| 2 | idx_mds_probalog_biztype_id |  | fid |

---

## 检修级别-多选基础资料表 t_mds_probalog_checktype

- **表名称：** 检修级别-多选基础资料表
- **表名：** t_mds_probalog_checktype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_check_id |  | fid |
| 2 | pk_mds_probalog_checktype |  | fpkid |

---

## 项目状态-多选基础资料表 t_mds_probalog_prostate

- **表名称：** 项目状态-多选基础资料表
- **表名：** t_mds_probalog_prostate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_pro_id |  | fid |
| 2 | pk_mds_probalog_prostate |  | fpkid |

---

## 检修设备类型-多选基础资料表 t_mds_probalog_actype

- **表名称：** 检修设备类型-多选基础资料表
- **表名：** t_mds_probalog_actype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_actype_id |  | fid |
| 2 | pk_mds_probalog_actype |  | fpkid |

---

## 客舱改装状态-多选基础资料表 t_mds_probalog_polaris

- **表名称：** 客舱改装状态-多选基础资料表
- **表名：** t_mds_probalog_polaris

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客舱改装状态 mds_polarisstatus |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_polaris_id |  | fid |
| 2 | pk_mds_probalog_polaris |  | fpkid |

---

## 历史单据体-子表 t_mds_probabilityhp_log

- **表名称：** 历史单据体-子表
- **表名：** t_mds_probabilityhp_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhpsortval | 排序值(后台) | text | 0 |  |  | null | 排序值(后台) |
| 3 | fhpdataselectnum | 数据选择条数 | int8 | 64 |  | √ | 0 | 数据选择条数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fhpselectdimension | 数据选择维度 | varchar | 255 |  | √ | ' ' | 数据选择维度 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fhpselectall | 全选 | bpchar | 1 |  | √ | '0' | 全选 |
| 8 | fhpselectdimensionval | 选择维度(后台) | varchar | 255 |  | √ | ' ' | 选择维度(后台) |
| 9 | fhpselectfilter | 选择条件 | varchar | 2000 |  | √ | ' ' | 选择条件 |
| 10 | fhpselectfilterval | 选择条件值(后台) | text | 0 |  |  | null | 选择条件值(后台) |
| 11 | fhpsort | 排序 | varchar | 2000 |  | √ | ' ' | 排序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probabilityhp_log |  | fentryid |
| 2 | idx_mds_probahp_log_id |  | fid |

---

## 用量概率计算日志-主表 t_mds_probabilitylog

- **表名称：** 用量概率计算日志-主表
- **表名：** t_mds_probabilitylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprobabilitycaldef | 方案编码 | int8 | 64 |  | √ | 0 | 用量概率计算方案定义 mds_probabilitycaldef |
| 3 | ferrmsg_tag | 日志详情_详情 | text | 0 |  |  | null | 日志详情_详情 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fhistorydata | 历史数据 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fsampledata | 样本数据 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 10 | fsamplehistoryfilter | 样本历史过滤字段对照 | varchar | 2000 |  | √ | ' ' | 样本历史过滤字段对照 |
| 11 | falgorithmdef | 用量概率算法 | int8 | 64 |  | √ | 0 | 用量概率算法定义 mds_algorithmdef |
| 12 | fcalstatus | 计算状态 | varchar | 5 |  | √ | ' ' | 计算状态,枚举: A :样本获取中 B :获取样本 C :历史获取中 D :获取历史 E :获取样本失败 F :获取历史失败 |
| 13 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fbackupproject | 备货项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 17 | fcountdim | 统计维度 | varchar | 50 |  | √ | ' ' | 统计维度,枚举: 1 :项目 2 :工卡 |
| 18 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fcommongroup | 分析维度（旧版） | varchar | 255 |  | √ | ' ' | 分析维度（旧版）,枚举: customer :客户 actype :检修设备类型 checktype :检修级别 cardtype :工卡类型 card :工卡号 |
| 20 | fanalysisdim | 分析维度 | varchar | 50 |  | √ | ' ' | 分析维度,枚举: A :客户+检修设备类型+检修级别 B :客户+检修设备类型 C :检修设备类型 |
| 21 | ferrmsg | 日志详情 | varchar | 255 |  | √ | ' ' | 日志详情 |
| 22 | fmaterialchange | 物料转换 | bpchar | 1 |  | √ | '0' | 物料转换 |
| 23 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 计算号 | varchar | 80 |  | √ | ' ' | 计算号 |
| 25 | fsamplehistoryfilterval | 样本历史过滤字段对照(后台) | text | 0 |  |  | null | 样本历史过滤字段对照(后台) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_number |  | fnumber |
| 2 | pk_mds_probabilitylog |  | fid |

---

## 客户-多选基础资料表 t_mds_probalog_customer

- **表名称：** 客户-多选基础资料表
- **表名：** t_mds_probalog_customer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probalog_cus_id |  | fid |
| 2 | pk_mds_probalog_customer |  | fpkid |

---

## 工卡号-多选基础资料表 t_mds_probalog_card

- **表名称：** 工卡号-多选基础资料表
- **表名：** t_mds_probalog_card

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probalog_card |  | fpkid |
| 2 | idx_mds_probalog_card_id |  | fid |

---

## 样本单据体-子表 t_mds_probabilitysp_log

- **表名称：** 样本单据体-子表
- **表名：** t_mds_probabilitysp_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspselectfilter | 选择条件 | varchar | 2000 |  | √ | ' ' | 选择条件 |
| 3 | fspselectfilterval | 选择条件值(后台) | text | 0 |  |  | null | 选择条件值(后台) |
| 4 | fspselectdimension | 数据选择维度 | varchar | 255 |  | √ | ' ' | 数据选择维度 |
| 5 | fspselectdimensionval | 选择维度(后台) | varchar | 255 |  | √ | ' ' | 选择维度(后台) |
| 6 | fspsort | 排序 | varchar | 2000 |  | √ | ' ' | 排序 |
| 7 | fspsortval | 排序值(后台) | text | 0 |  |  | null | 排序值(后台) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fspselectall | 全选 | bpchar | 1 |  | √ | '0' | 全选 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fspdataselectnum | 数据选择条数 | int8 | 64 |  | √ | 0 | 数据选择条数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probasp_log_id |  | fid |
| 2 | pk_mds_probabilitysp_log |  | fentryid |

---

## 工卡类型-多选基础资料表 t_mds_probalog_cardtype

- **表名称：** 工卡类型-多选基础资料表
- **表名：** t_mds_probalog_cardtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工卡类型 mpdm_jobcardtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probalog_cardtype |  | fpkid |
| 2 | idx_mds_probalog_cardt_id |  | fid |
