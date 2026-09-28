# 生产领料申请变更日志-im_mdc_mrbchangelog

## 生产领料申请变更日志-主表 t_im_mdc_mrbchangelog

- **表名称：** 生产领料申请变更日志-主表
- **表名：** t_im_mdc_mrbchangelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 5 | fxreqbillno | 生产领料申请变更单号 | varchar | 50 |  | √ | ' ' | 生产领料申请变更单号 |
| 6 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | freqbillno | 生产领料申请单号 | varchar | 50 |  | √ | ' ' | 生产领料申请单号 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | freason | 变更原因 | varchar | 50 |  | √ | ' ' | 变更原因 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :变更中 C :变更完成 |
| 12 | freqbillid | 申请单id | int8 | 64 |  | √ | 0 | 申请单id |
| 13 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmftreqentryf7 | 生产领料申请分录F7 | int8 | 64 |  | √ | 0 | [生产领料申请分录F7 im_mdc_mftreqentryf7](../im_files/im_mdc_mftreqentryf7.md) |
| 15 | fxreqentryid | 变更单分录id | int8 | 64 |  | √ | 0 | 变更单分录id |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fxreqbillid | 变更单id | int8 | 64 |  | √ | 0 | 变更单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_mrl_freqbillid |  | freqbillid |
| 2 | pk_im_mdc_mrbchangelog |  | fid |
| 3 | idx_mdc_mrl_fxreqbillid |  | fxreqbillid |
| 4 | idx_mdc_mrl_fmftreqentryf7 |  | fmftreqentryf7 |
| 5 | idx_mdc_mrl_fxreqentryid |  | fxreqentryid |

---

## 单据体-子表 t_im_mdc_mrblogentry

- **表名称：** 单据体-子表
- **表名：** t_im_mdc_mrblogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 申请数量 | varchar | 50 |  | √ | ' ' | 申请数量 |
| 3 | freqentryf7 | 领料申请变更分录f7 | int8 | 64 |  | √ | 0 | [生产领料申请变更分录F7 im_mdc_xmftreqentryf7](../im_files/im_mdc_xmftreqentryf7.md) |
| 4 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | flocation | 供货仓位 | varchar | 50 |  | √ | ' ' | 供货仓位 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdelivertime | 配送时间 | varchar | 50 |  | √ | ' ' | 配送时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 |
| 11 | fwarehouse | 供货仓库 | varchar | 50 |  | √ | ' ' | 供货仓库 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_mrblogentry |  | fentryid |
| 2 | idx_mdc_mrblogentry_fid |  | fid |
