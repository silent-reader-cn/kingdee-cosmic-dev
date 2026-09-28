# 渠道销售计划-occbo_deptsaleplan

## 渠道销售计划-主表 t_occbo_deptsaleplan

- **表名称：** 渠道销售计划-主表
- **表名：** t_occbo_deptsaleplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fassessentityid | 滚动计划月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 3 | fname | 计划名称 | varchar | 80 |  | √ | ' ' | 计划名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuserid | 计划人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fdepartmentid | 计划部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fplanstatus | 滚动计划状态 | bpchar | 1 |  | √ | 'A' | 滚动计划状态,枚举: A :滚动编制中 B :编制完成 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fassessperiodid | 计划年份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 16 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbillno | 计划编号 | varchar | 80 |  | √ | ' ' | 计划编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbilltypeid | 计划方案 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_deptsaleplan_billno |  | fbillno |
| 2 | pk_occbo_deptsaleplan |  | fid |

---

## 计划明细-子表 t_occbo_deptsaleplan_ee

- **表名称：** 计划明细-子表
- **表名：** t_occbo_deptsaleplan_ee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpresentqty4 | 赠品数量4 | numeric | 23 | 10 | √ | 0 | 赠品数量4 |
| 3 | fpresentqty3 | 赠品数量3 | numeric | 23 | 10 | √ | 0 | 赠品数量3 |
| 4 | fpresentqty2 | 赠品数量2 | numeric | 23 | 10 | √ | 0 | 赠品数量2 |
| 5 | fpresentqty1 | 赠品数量1 | numeric | 23 | 10 | √ | 0 | 赠品数量1 |
| 6 | fpresentqty8 | 赠品数量8 | numeric | 23 | 10 | √ | 0 | 赠品数量8 |
| 7 | fpresentqty7 | 赠品数量7 | numeric | 23 | 10 | √ | 0 | 赠品数量7 |
| 8 | fpresentqty6 | 赠品数量6 | numeric | 23 | 10 | √ | 0 | 赠品数量6 |
| 9 | ftotalqty9 | 计划总数量9 | numeric | 23 | 10 | √ | 0 | 计划总数量9 |
| 10 | fpresentqty5 | 赠品数量5 | numeric | 23 | 10 | √ | 0 | 赠品数量5 |
| 11 | ftotalqty8 | 计划总数量8 | numeric | 23 | 10 | √ | 0 | 计划总数量8 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | fpresentqty9 | 赠品数量9 | numeric | 23 | 10 | √ | 0 | 赠品数量9 |
| 14 | fdifferenceqty | 填报差异数 | numeric | 23 | 10 | √ | 0 | 填报差异数 |
| 15 | ftargetqty8 | 目标数量8 | numeric | 23 | 10 | √ | 0 | 目标数量8 |
| 16 | ftargetqty7 | 目标数量7 | numeric | 23 | 10 | √ | 0 | 目标数量7 |
| 17 | ftargetqty9 | 目标数量9 | numeric | 23 | 10 | √ | 0 | 目标数量9 |
| 18 | ftargetqty4 | 目标数量4 | numeric | 23 | 10 | √ | 0 | 目标数量4 |
| 19 | flastqty10 | 去年数量10 | numeric | 23 | 10 | √ | 0 | 去年数量10 |
| 20 | ftargetqty3 | 目标数量3 | numeric | 23 | 10 | √ | 0 | 目标数量3 |
| 21 | ftargetqty6 | 目标数量6 | numeric | 23 | 10 | √ | 0 | 目标数量6 |
| 22 | flastqty12 | 去年数量12 | numeric | 23 | 10 | √ | 0 | 去年数量12 |
| 23 | ftargetqty5 | 目标数量5 | numeric | 23 | 10 | √ | 0 | 目标数量5 |
| 24 | flastqty11 | 去年数量11 | numeric | 23 | 10 | √ | 0 | 去年数量11 |
| 25 | ftargetqty2 | 目标数量2 | numeric | 23 | 10 | √ | 0 | 目标数量2 |
| 26 | ftargetqty1 | 目标数量1 | numeric | 23 | 10 | √ | 0 | 目标数量1 |
| 27 | fitemid | 产品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 28 | fitemqty2 | 正品数量2 | numeric | 23 | 10 | √ | 0 | 正品数量2 |
| 29 | fitemqty1 | 正品数量1 | numeric | 23 | 10 | √ | 0 | 正品数量1 |
| 30 | fitemqty4 | 正品数量4 | numeric | 23 | 10 | √ | 0 | 正品数量4 |
| 31 | fitemqty3 | 正品数量3 | numeric | 23 | 10 | √ | 0 | 正品数量3 |
| 32 | fitemqty6 | 正品数量6 | numeric | 23 | 10 | √ | 0 | 正品数量6 |
| 33 | ftotalqty7 | 计划总数量7 | numeric | 23 | 10 | √ | 0 | 计划总数量7 |
| 34 | fitemqty5 | 正品数量5 | numeric | 23 | 10 | √ | 0 | 正品数量5 |
| 35 | ftotalqty6 | 计划总数量6 | numeric | 23 | 10 | √ | 0 | 计划总数量6 |
| 36 | fitemqty8 | 正品数量8 | numeric | 23 | 10 | √ | 0 | 正品数量8 |
| 37 | ftotalqty5 | 计划总数量5 | numeric | 23 | 10 | √ | 0 | 计划总数量5 |
| 38 | ftargetqty11 | 目标数量11 | numeric | 23 | 10 | √ | 0 | 目标数量11 |
| 39 | fitemqty7 | 正品数量7 | numeric | 23 | 10 | √ | 0 | 正品数量7 |
| 40 | ftotalqty4 | 计划总数量4 | numeric | 23 | 10 | √ | 0 | 计划总数量4 |
| 41 | ftargetqty10 | 目标数量10 | numeric | 23 | 10 | √ | 0 | 目标数量10 |
| 42 | ftotalqty3 | 计划总数量3 | numeric | 23 | 10 | √ | 0 | 计划总数量3 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | fitemqty9 | 正品数量9 | numeric | 23 | 10 | √ | 0 | 正品数量9 |
| 45 | ftotalqty2 | 计划总数量2 | numeric | 23 | 10 | √ | 0 | 计划总数量2 |
| 46 | ftotalqty1 | 计划总数量1 | numeric | 23 | 10 | √ | 0 | 计划总数量1 |
| 47 | fpresentqty11 | 赠品数量11 | numeric | 23 | 10 | √ | 0 | 赠品数量11 |
| 48 | fpresentqty10 | 赠品数量10 | numeric | 23 | 10 | √ | 0 | 赠品数量10 |
| 49 | fpresentqty12 | 赠品数量12 | numeric | 23 | 10 | √ | 0 | 赠品数量12 |
| 50 | ftotalqty | 全年预测数 | numeric | 23 | 10 | √ | 0 | 全年预测数 |
| 51 | ftargetqty12 | 目标数量12 | numeric | 23 | 10 | √ | 0 | 目标数量12 |
| 52 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 53 | ftotaltodoqty | 全年待完成 | numeric | 23 | 10 | √ | 0 | 全年待完成 |
| 54 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 55 | fitemqty11 | 正品数量11 | numeric | 23 | 10 | √ | 0 | 正品数量11 |
| 56 | fitemqty10 | 正品数量10 | numeric | 23 | 10 | √ | 0 | 正品数量10 |
| 57 | fitemqty12 | 正品数量12 | numeric | 23 | 10 | √ | 0 | 正品数量12 |
| 58 | flastqty1 | 去年数量1 | numeric | 23 | 10 | √ | 0 | 去年数量1 |
| 59 | ftotalqty10 | 计划总数量10 | numeric | 23 | 10 | √ | 0 | 计划总数量10 |
| 60 | ftotalqty12 | 计划总数量12 | numeric | 23 | 10 | √ | 0 | 计划总数量12 |
| 61 | flastqty6 | 去年数量6 | numeric | 23 | 10 | √ | 0 | 去年数量6 |
| 62 | ftotalactualqty | 全年实际数 | numeric | 23 | 10 | √ | 0 | 全年实际数 |
| 63 | ftotalqty11 | 计划总数量11 | numeric | 23 | 10 | √ | 0 | 计划总数量11 |
| 64 | flastqty7 | 去年数量7 | numeric | 23 | 10 | √ | 0 | 去年数量7 |
| 65 | flastqty8 | 去年数量8 | numeric | 23 | 10 | √ | 0 | 去年数量8 |
| 66 | flastqty9 | 去年数量9 | numeric | 23 | 10 | √ | 0 | 去年数量9 |
| 67 | flastqty2 | 去年数量2 | numeric | 23 | 10 | √ | 0 | 去年数量2 |
| 68 | flastqty3 | 去年数量3 | numeric | 23 | 10 | √ | 0 | 去年数量3 |
| 69 | flastqty4 | 去年数量4 | numeric | 23 | 10 | √ | 0 | 去年数量4 |
| 70 | flastqty5 | 去年数量5 | numeric | 23 | 10 | √ | 0 | 去年数量5 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_deptsaleplanee_fid |  | fid |
| 2 | pk_occbo_deptsaleplan_ee |  | fentryid |

---

## 计划明细-分表 t_occbo_deptsaleplan_ee_e

- **表名称：** 计划明细-分表
- **表名：** t_occbo_deptsaleplan_ee_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemactualqty10 | 实际正品数量10 | numeric | 23 | 10 | √ | 0 | 实际正品数量10 |
| 3 | fitemactualqty11 | 实际正品数量11 | numeric | 23 | 10 | √ | 0 | 实际正品数量11 |
| 4 | fitemactualqty12 | 实际正品数量12 | numeric | 23 | 10 | √ | 0 | 实际正品数量12 |
| 5 | fpresentactualqty4 | 实际赠品数量4 | numeric | 23 | 10 | √ | 0 | 实际赠品数量4 |
| 6 | ftotalactualqty10 | 实际总数量10 | numeric | 23 | 10 | √ | 0 | 实际总数量10 |
| 7 | fpresentactualqty3 | 实际赠品数量3 | numeric | 23 | 10 | √ | 0 | 实际赠品数量3 |
| 8 | fpresentactualqty6 | 实际赠品数量6 | numeric | 23 | 10 | √ | 0 | 实际赠品数量6 |
| 9 | ftotalactualqty12 | 实际总数量12 | numeric | 23 | 10 | √ | 0 | 实际总数量12 |
| 10 | fpresentactualqty5 | 实际赠品数量5 | numeric | 23 | 10 | √ | 0 | 实际赠品数量5 |
| 11 | ftotalactualqty11 | 实际总数量11 | numeric | 23 | 10 | √ | 0 | 实际总数量11 |
| 12 | fpresentactualqty8 | 实际赠品数量8 | numeric | 23 | 10 | √ | 0 | 实际赠品数量8 |
| 13 | fpresentactualqty7 | 实际赠品数量7 | numeric | 23 | 10 | √ | 0 | 实际赠品数量7 |
| 14 | fpresentactualqty9 | 实际赠品数量9 | numeric | 23 | 10 | √ | 0 | 实际赠品数量9 |
| 15 | fpresentactualqty12 | 实际赠品数量12 | numeric | 23 | 10 | √ | 0 | 实际赠品数量12 |
| 16 | fpresentactualqty11 | 实际赠品数量11 | numeric | 23 | 10 | √ | 0 | 实际赠品数量11 |
| 17 | fpresentactualqty2 | 实际赠品数量2 | numeric | 23 | 10 | √ | 0 | 实际赠品数量2 |
| 18 | fpresentactualqty10 | 实际赠品数量10 | numeric | 23 | 10 | √ | 0 | 实际赠品数量10 |
| 19 | fpresentactualqty1 | 实际赠品数量1 | numeric | 23 | 10 | √ | 0 | 实际赠品数量1 |
| 20 | fitemactualqty1 | 实际正品数量1 | numeric | 23 | 10 | √ | 0 | 实际正品数量1 |
| 21 | ftotalactualqty2 | 实际总数量2 | numeric | 23 | 10 | √ | 0 | 实际总数量2 |
| 22 | fitemactualqty2 | 实际正品数量2 | numeric | 23 | 10 | √ | 0 | 实际正品数量2 |
| 23 | ftotalactualqty3 | 实际总数量3 | numeric | 23 | 10 | √ | 0 | 实际总数量3 |
| 24 | ftotalactualqty4 | 实际总数量4 | numeric | 23 | 10 | √ | 0 | 实际总数量4 |
| 25 | ftotalactualqty5 | 实际总数量5 | numeric | 23 | 10 | √ | 0 | 实际总数量5 |
| 26 | fitemactualqty5 | 实际正品数量5 | numeric | 23 | 10 | √ | 0 | 实际正品数量5 |
| 27 | ftotalactualqty6 | 实际总数量6 | numeric | 23 | 10 | √ | 0 | 实际总数量6 |
| 28 | fitemactualqty6 | 实际正品数量6 | numeric | 23 | 10 | √ | 0 | 实际正品数量6 |
| 29 | ftotalactualqty7 | 实际总数量7 | numeric | 23 | 10 | √ | 0 | 实际总数量7 |
| 30 | fitemactualqty3 | 实际正品数量3 | numeric | 23 | 10 | √ | 0 | 实际正品数量3 |
| 31 | ftotalactualqty8 | 实际总数量8 | numeric | 23 | 10 | √ | 0 | 实际总数量8 |
| 32 | fitemactualqty4 | 实际正品数量4 | numeric | 23 | 10 | √ | 0 | 实际正品数量4 |
| 33 | ftotalactualqty9 | 实际总数量9 | numeric | 23 | 10 | √ | 0 | 实际总数量9 |
| 34 | fitemactualqty9 | 实际正品数量9 | numeric | 23 | 10 | √ | 0 | 实际正品数量9 |
| 35 | fitemactualqty7 | 实际正品数量7 | numeric | 23 | 10 | √ | 0 | 实际正品数量7 |
| 36 | fitemactualqty8 | 实际正品数量8 | numeric | 23 | 10 | √ | 0 | 实际正品数量8 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 38 | ftotalactualqty1 | 实际总数量1 | numeric | 23 | 10 | √ | 0 | 实际总数量1 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_deptsaleplan_ee_e |  | fentryid |
| 2 | idx_occbo_deptsaleplaneee_fid |  | fid |
