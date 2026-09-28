# 更新申请单-sco_costupdatenew

## 单据体-子表 t_sco_costupdatematerials

- **表名称：** 单据体-子表
- **表名：** t_sco_costupdatematerials

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatversion | fmatversion | int8 | 64 |  | √ | 0 |  |
| 3 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fmatgrpid | fmatgrpid | int8 | 64 |  | √ | 0 |  |
| 6 | fsalcalclogid | fsalcalclogid | int8 | 64 |  | √ | 0 |  |
| 7 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fauxprop | fauxprop | int8 | 64 |  | √ | 0 |  |
| 10 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 11 | flot | flot | varchar | 80 |  | √ | ' ' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costupdatematerials |  | fentryid |
| 2 | index_sco_costupdatemats_df |  | fmaterialid,fmatversion,fauxprop |

---

## 更新申请单-主表 t_sco_costupdatenew

- **表名称：** 更新申请单-主表
- **表名：** t_sco_costupdatenew

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fresmatbyuseauxpt_tag | fresmatbyuseauxpt_tag | text | 0 |  |  | null |  |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fupdatebillno | 确认单编号 | varchar | 80 |  | √ | ' ' | 确认单编号 |
| 6 | ftargetcosttype | 目标标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 7 | fresbynoref | fresbynoref | varchar | 2000 |  | √ | ' ' |  |
| 8 | fupdatestatus | 更新状态 | varchar | 30 |  | √ | ' ' | 更新状态,枚举: N :未完成 Y :已完成 |
| 9 | fresmatbyuseauxpt | fresmatbyuseauxpt | varchar | 2000 |  | √ | ' ' |  |
| 10 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fperiodid | 生效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 13 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fsrccosttype | 源标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 17 | fisquickupdate | 来源于快速更新 | bpchar | 1 |  | √ | '0' | 来源于快速更新 |
| 18 | fiscalccurlevel | 仅更新本层 | bpchar | 1 |  | √ | '0' | 仅更新本层 |
| 19 | fisspecifymaterial | fisspecifymaterial | bpchar | 1 |  | √ | '0' |  |
| 20 | fmatgrpstdid | fmatgrpstdid | int8 | 64 |  | √ | 0 |  |
| 21 | fupdatebillid | 确认单ID | int8 | 64 |  | √ | 0 | 确认单ID |
| 22 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 23 | feffecttime | feffecttime | timestamp | 0 |  |  | null |  |
| 24 | fresbynoref_tag | fresbynoref_tag | text | 0 |  |  | null |  |
| 25 | fisallupdate | 全量更新 | bpchar | 1 |  | √ | '0' | 全量更新 |
| 26 | fsourcepage | fsourcepage | varchar | 50 |  | √ | ' ' |  |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costupdatenew |  | fid |
| 2 | index_sco_costupdatenew_df |  | fsrccosttype,ftargetcosttype |
