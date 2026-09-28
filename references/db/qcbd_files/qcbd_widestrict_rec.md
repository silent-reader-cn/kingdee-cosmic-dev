# 宽严度转换记录-qcbd_widestrict_rec

## 转换履历-子表 t_qcbd_wsrec_ety

- **表名称：** 转换履历-子表
- **表名：** t_qcbd_wsrec_ety

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauditnum | 审核次数 | int4 | 32 |  | √ | 0 | 审核次数 |
| 3 | fdeletedt | 删除时间 | timestamp | 0 |  |  | null | 删除时间 |
| 4 | fbillentry | 分录内码 | varchar | 50 |  | √ | ' ' | 分录内码 |
| 5 | fauditdtfst | 首次审核时间 | timestamp | 0 |  |  | null | 首次审核时间 |
| 6 | fetyinspectproid | 检验方案 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 7 | frecvdate | 检验单创建时间 | timestamp | 0 |  |  | null | 检验单创建时间 |
| 8 | fdfwsstageid | 宽严度转换阶段（检验用） | int8 | 64 |  | √ | 0 | [宽严度阶段 qcbd_widstrict_stage](../qcbd_files/qcbd_widstrict_stage.md) |
| 9 | fwsstageid | 宽严度转换阶段(计算用) | int8 | 64 |  | √ | 0 | [宽严度阶段 qcbd_widstrict_stage](../qcbd_files/qcbd_widstrict_stage.md) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 12 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: unaudit :暂存 audit :已审核 delete :已删除 |
| 13 | fetywsruleid | 宽严度转换方案 | int8 | 64 |  | √ | 0 | [宽严度转换方案 qcbd_widstrict_rule](../qcbd_files/qcbd_widstrict_rule.md) |
| 14 | funauditdtlast | 最终反审核时间 | timestamp | 0 |  |  | null | 最终反审核时间 |
| 15 | fbillid | 单据内码 | varchar | 50 |  | √ | ' ' | 单据内码 |
| 16 | fauditdtlast | 最终审核时间 | timestamp | 0 |  |  | null | 最终审核时间 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fetybillno | 检验单单据编号 | varchar | 50 |  | √ | ' ' | 检验单单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_wsreec_fid |  | fid |
| 2 | idx_qcbd_wsreec_fseq |  | fseq |
| 3 | pk_qcbd_wsrec_ety |  | fentryid |

---

## 宽严度转换记录-主表 t_qcbd_wdstrt_rec

- **表名称：** 宽严度转换记录-主表
- **表名：** t_qcbd_wdstrt_rec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: |
| 3 | fcreatetime | 转换方案生效时间 | timestamp | 0 |  |  | null | 转换方案生效时间 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fjpendtm | 跳批截止时间 | timestamp | 0 |  |  | null | 跳批截止时间 |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcurstageid | 当前检验阶段 | int8 | 64 |  | √ | 0 | [宽严度阶段 qcbd_widstrict_stage](../qcbd_files/qcbd_widstrict_stage.md) |
| 8 | finspectauditdate | 计算检验单审核时间 | timestamp | 0 |  |  | null | 计算检验单审核时间 |
| 9 | fsapplanid | 抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 10 | fsrcbill | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: qcp_incominginspct :来料检验单 qcpp_manuinspec :生产检验单 |
| 11 | finspectproid | 当前检验方案 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | feffdtend | 检验阶段重置时间 | timestamp | 0 |  |  | null | 检验阶段重置时间 |
| 14 | fwsruleid | 当前宽严度转换方案 | int8 | 64 |  | √ | 0 | [宽严度转换方案 qcbd_widstrict_rule](../qcbd_files/qcbd_widstrict_rule.md) |
| 15 | foprworkshopid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fjpleftnum | 跳批剩余批数 | int8 | 64 |  | √ | 0 | 跳批剩余批数 |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fbillno | 计算检验单单据编号 | varchar | 30 |  | √ | ' ' | 计算检验单单据编号 |
| 19 | fnexstageid | 下批检验阶段 | int8 | 64 |  | √ | 0 | [宽严度阶段 qcbd_widstrict_stage](../qcbd_files/qcbd_widstrict_stage.md) |
| 20 | fbilltypeid | 单据类型内码 | int8 | 64 |  | √ | 0 | 单据类型内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_wdstrt_fbillno |  | fbillno |
| 2 | idx_qcbd_wdstrt_fcreatetime |  | fcreatetime |
| 3 | pk_qcbd_wdstrt_rec |  | fid |
