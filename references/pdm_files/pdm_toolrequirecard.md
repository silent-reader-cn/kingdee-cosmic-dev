# 待维护工具需求工卡清单（废弃）-pdm_toolrequirecard

## 关联子实体-子表 t_pdm_entryrequirecard_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pdm_entryrequirecard_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_entryrequirecard_lk |  | fpkid |
| 2 | idx_pdm_entryrequirecard_lk_fk |  | fentryid |

---

## 待维护工具需求工卡清单（废弃）-关联追踪表 t_pdm_toolrequirecard_tc

- **表名称：** 待维护工具需求工卡清单（废弃）-关联追踪表
- **表名：** t_pdm_toolrequirecard_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_toolrequirecard_tc_tbill |  | ftbillid |
| 2 | pk_pdm_toolrequirecard_tc |  | fid |
| 3 | idx_pdm_toolrequirecard_tc_tid |  | ftid |

---

## 关联子实体-子表 t_pdm_toolrequirecard_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pdm_toolrequirecard_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_toolrequirecard_lk_fk |  | fid |
| 2 | pk_pdm_toolrequirecard_lk |  | fpkid |

---

## 子单据体-子表 t_pdm_tluserentry

- **表名称：** 子单据体-子表
- **表名：** t_pdm_tluserentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 2 | fuserid | 维护人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_tluserentry |  | fdetailid |
| 2 | idx_pdm_tlusry_fentryid |  | fentryid |

---

## 维护人员-多选基础资料表 t_pdm_toolmuluser

- **表名称：** 维护人员-多选基础资料表
- **表名：** t_pdm_toolmuluser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_toolmuluser_fk |  | fentryid |
| 2 | pk_pdm_toolmuluser |  | fpkid |

---

## 单据体-子表 t_pdm_entryrequirecard

- **表名称：** 单据体-子表
- **表名：** t_pdm_entryrequirecard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequiretool | 需要工具(封存) | varchar | 50 |  | √ | ' ' | 需要工具(封存),枚举: A :待确认 B :需要 C :不需要 |
| 3 | ftoolstatus | 工卡工具需求维护状态 | varchar | 50 |  | √ | ' ' | 工卡工具需求维护状态,枚举: A :未开始 B :已分配 C :已完成 D :取消 |
| 4 | fmoddate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fmoduser | 修改人 | varchar | 50 |  | √ | ' ' | 人员 bos_user |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fworkcardtoolid | 工卡工具需求 | int8 | 64 |  | √ | 0 | 工卡工具需求 mpdm_cardtooldemand |
| 9 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 10 | fcardnum | 工卡编码 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_entryrequirecard |  | fentryid |
| 2 | idx_pdm_entryrequirecard |  | fid |
| 3 | idx_pdm_entryrequire_cardnum |  | fcardnum |

---

## 待维护工具需求工卡清单（废弃）-主表 t_pdm_toolrequirecard

- **表名称：** 待维护工具需求工卡清单（废弃）-主表
- **表名：** t_pdm_toolrequirecard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenginetype | 发动机型号 | int8 | 64 |  | √ | 0 | 发动机型号 mpdm_enginetype |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmratype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fprojectnum | 项目编码 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fcheckregno | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 11 | fsource | 单据来源 | varchar | 5 |  | √ | ' ' | 单据来源,枚举: A :工作包 B :项目范围 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fprojectrange | 项目范围 | int8 | 64 |  | √ | 0 | 项目范围F7（废弃） pdm_projectscope_f7 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftoolcreatestatus | 工卡工具创建状态 | varchar | 50 |  | √ | ' ' | 工卡工具创建状态,枚举: A :未完成 B :已完成 |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_toolrequirecard |  | fbillno |
| 2 | pk_pdm_toolrequirecard |  | fid |

---

## 待维护工具需求工卡清单（废弃）-反写记录表 t_pdm_toolrequirecard_wb

- **表名称：** 待维护工具需求工卡清单（废弃）-反写记录表
- **表名：** t_pdm_toolrequirecard_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_toolrequirecard_wb |  | fentryid |
| 2 | idx_pdm_toolrequirecard_wb_fk |  | fid |
