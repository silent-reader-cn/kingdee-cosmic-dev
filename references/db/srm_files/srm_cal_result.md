# 计算结果详情-srm_cal_result

## 单据体-子表 t_pur_calresultentity

- **表名称：** 单据体-子表
- **表名：** t_pur_calresultentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fresult | 计算结果 | numeric | 23 | 10 | √ | 0 | 计算结果 |
| 5 | fresult2 | 子公式2结果 | numeric | 23 | 10 | √ | 0 | 子公式2结果 |
| 6 | fresult1 | 子公式1结果 | numeric | 23 | 10 | √ | 0 | 子公式1结果 |
| 7 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fresult5 | 子公式5结果 | numeric | 23 | 10 | √ | 0 | 子公式5结果 |
| 9 | fstatus | 计算状态 | bpchar | 1 |  | √ | ' ' | 计算状态,枚举: A :未计算 B :计算中 C :已完成 D :计算异常 |
| 10 | fresult4 | 子公式4结果 | numeric | 23 | 10 | √ | 0 | 子公式4结果 |
| 11 | fresult3 | 子公式3结果 | numeric | 23 | 10 | √ | 0 | 子公式3结果 |
| 12 | findexscoredetailid | 评估任务明细id | int8 | 64 |  | √ | 0 | 评估任务明细id |
| 13 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fscoretaskid | 评估任务id | int8 | 64 |  | √ | 0 | 评估任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_calresultentity |  | fentryid |
| 2 | idx_pur_calresulte_fid_fseq |  | fid,fseq |

---

## 计算结果详情-主表 t_pur_calresult

- **表名称：** 计算结果详情-主表
- **表名：** t_pur_calresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fformulatran | 结果集公式译文 | varchar | 1000 |  | √ | ' ' | 结果集公式译文 |
| 4 | fdateto | 评估期间至 | timestamp | 0 |  |  | null | 评估期间至 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fevaplanid | 评估计划id | int8 | 64 |  | √ | 0 | 评估计划id |
| 9 | fsrmindex | 评估指标 | int8 | 64 |  | √ | 0 | 评估指标 srm_index |
| 10 | fevaplanname | 评估计划名称 | varchar | 100 |  | √ | ' ' | 评估计划名称 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fcalformula | 计算公式 | int8 | 64 |  | √ | 0 | 计算公式配置 srm_cal_formula |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fformula | 结果集公式 | varchar | 500 |  | √ | ' ' | 结果集公式 |
| 16 | fevadimension | 评估方式 | bpchar | 1 |  | √ | ' ' | 评估方式,枚举: A :按供应商维度 B :按物料维度 D :按品类评估 |
| 17 | fdatefrom | 评估期间从 | timestamp | 0 |  |  | null | 评估期间从 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_calresult_cluster |  | forgid,fsrmindex,fevaplanid,fevadimension |
| 2 | idx_pur_calresult_fbillno |  | fbillno |
| 3 | pk_pur_calresult |  | fid |
