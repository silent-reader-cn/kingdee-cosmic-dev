# 用料明细变更日志-pom_xmfstockchangelog

## 单据体-子表 t_pom_stockchglogdetail

- **表名称：** 单据体-子表
- **表名：** t_pom_stockchglogdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funissueqty | 未发数量 | varchar | 50 |  | √ | ' ' | 未发数量 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | fwastagerateformula | 损耗计算公式 | varchar | 50 |  | √ | ' ' | 损耗计算公式 |
| 5 | fstandqty | 标准基本数量 | varchar | 50 |  | √ | ' ' | 标准基本数量 |
| 6 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式 |
| 7 | flocation | 仓位 | varchar | 50 |  | √ | ' ' | 仓位 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | foutlocation | 调出仓位 | varchar | 50 |  | √ | ' ' | 调出仓位 |
| 10 | fscraprate | 变动损耗率 | varchar | 50 |  | √ | ' ' | 变动损耗率 |
| 11 | fdemanddate | 需求日期 | varchar | 50 |  | √ | ' ' | 需求日期 |
| 12 | fuseqty | 已消耗数量 | varchar | 50 |  | √ | ' ' | 已消耗数量 |
| 13 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 14 | foutorgunitid | 调出组织 | varchar | 50 |  | √ | ' ' | 调出组织 |
| 15 | foverissuecontrl | 超发控制 | varchar | 50 |  | √ | ' ' | 超发控制 |
| 16 | fissinlowlimit | 领料下限允差% | varchar | 50 |  | √ | ' ' | 领料下限允差% |
| 17 | fissinhighlimit | 领料上限允差% | varchar | 50 |  | √ | ' ' | 领料上限允差% |
| 18 | fuseratio | 使用比例 | numeric | 10 | 2 | √ | 0.00 | 使用比例 |
| 19 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 20 | fqtydenominator | 分母 | varchar | 50 |  | √ | ' ' | 分母 |
| 21 | fqtynumerator | 分子 | varchar | 50 |  | √ | ' ' | 分子 |
| 22 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲 |
| 23 | fwarehouseid | 仓库 | varchar | 50 |  | √ | ' ' | 仓库 |
| 24 | flackraitioqty | 领料下限数量 | varchar | 50 |  | √ | ' ' | 领料下限数量 |
| 25 | fsupplierid | 货主 | varchar | 50 |  | √ | ' ' | 货主 |
| 26 | fiskeypart | 关键件 | varchar | 50 |  | √ | ' ' | 关键件 |
| 27 | ffixscrap | 固定损耗 | varchar | 50 |  | √ | ' ' | 固定损耗 |
| 28 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型 |
| 29 | foutwarehouseid | 调出仓库 | varchar | 50 |  | √ | ' ' | 调出仓库 |
| 30 | fwipqty | 在制数量 | varchar | 50 |  | √ | ' ' | 在制数量 |
| 31 | fisbulkmaterial | 散装物料 | varchar | 50 |  | √ | ' ' | 散装物料 |
| 32 | fdemandqty | 需求基本数量 | varchar | 50 |  | √ | ' ' | 需求基本数量 |
| 33 | fcansendqty | 可发数量 | varchar | 50 |  | √ | ' ' | 可发数量 |
| 34 | fsupplyorgid | 供货库存组织 | varchar | 50 |  | √ | ' ' | 供货库存组织 |
| 35 | fextraratioqty | 领料上限数量 | varchar | 50 |  | √ | ' ' | 领料上限数量 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 |
| 38 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_stockchglogdetail |  | fentryid |
| 2 | idx_pom_stockchglogdetail_fid |  | fid |

---

## 用料明细变更日志-主表 t_pom_xmfstockchangelog

- **表名称：** 用料明细变更日志-主表
- **表名：** t_pom_xmfstockchangelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :变更中 C :变更完成 |
| 4 | fstockentryseq | 组件清单行号 | varchar | 50 |  | √ | ' ' | 组件清单行号 |
| 5 | fcreatetime | 变更单时间 | timestamp | 0 |  |  | null | 变更单时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fentryidf | 组件清单分录f7 | int8 | 64 |  | √ | 0 | 生产组件清单分录f7 pom_mftstockentryf7 |
| 8 | fstockid | 组件清单id | varchar | 50 |  | √ | ' ' | 组件清单id |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | freason | 变更原因 | varchar | 50 |  | √ | ' ' | 变更原因 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstockentryid | 组件清单分录id | varchar | 50 |  | √ | ' ' | 组件清单分录id |
| 13 | fstockno | 用料清单编码 | varchar | 50 |  | √ | ' ' | 用料清单编码 |
| 14 | fchangeno | 变更单编码 | varchar | 50 |  | √ | ' ' | 变更单编码 |
| 15 | fstockchangeentryid | 变更单分录id | varchar | 50 |  | √ | ' ' | 变更单分录id |
| 16 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fstockchangeentryseq | 变更单行号 | varchar | 50 |  | √ | ' ' | 变更单行号 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fstockchangeid | 变更单id | varchar | 50 |  | √ | ' ' | 变更单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_xmfstockchangelog_id |  | fstockid |
| 2 | pk_pom_xmfstockchangelog |  | fid |
