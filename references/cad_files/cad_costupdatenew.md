# 更新申请单-cad_costupdatenew

## 更新申请单-主表 t_cad_costupdatenew

- **表名称：** 更新申请单-主表
- **表名：** t_cad_costupdatenew

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fresmatbyuseauxpt_tag | 资源快速更新启用辅助属性的物料_详情 | text | 0 |  |  | null | 资源快速更新启用辅助属性的物料_详情 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fupdatebillno | 确认单编号 | varchar | 80 |  | √ | ' ' | 确认单编号 |
| 6 | ftargetcosttype | 目标成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 7 | fresbynoref | 未被引用的资源 | varchar | 2000 |  | √ | ' ' | 未被引用的资源 |
| 8 | fupdatestatus | 更新状态 | varchar | 80 |  | √ | ' ' | 更新状态,枚举: N :未完成 Y :已完成 |
| 9 | fresmatbyuseauxpt | 资源快速更新启用辅助属性的物料 | varchar | 2000 |  | √ | ' ' | 资源快速更新启用辅助属性的物料 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fperiodid | 生效期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 13 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fsrccosttype | 源成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 17 | fiscalccurlevel | 仅更新本层 | bpchar | 1 |  | √ | '0' | 仅更新本层 |
| 18 | fisspecifymaterial | 指定物料更新 | bpchar | 1 |  | √ | '0' | 指定物料更新 |
| 19 | fmatgrpstdid | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 bd_materialgroupstandard |
| 20 | fupdatebillid | 确认单ID | int8 | 64 |  | √ | 0 | 确认单ID |
| 21 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 22 | feffecttime | feffecttime | timestamp | 0 |  |  | null |  |
| 23 | fresbynoref_tag | 未被引用的资源_详情 | text | 0 |  |  | null | 未被引用的资源_详情 |
| 24 | fisallupdate | 全量更新 | bpchar | 1 |  | √ | '0' | 全量更新 |
| 25 | fsourcepage | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_costupdatenew_pkey |  | fid |
| 2 | index_cad_costupdatenew_df |  | fsrccosttype,ftargetcosttype |

---

## 单据体-子表 t_cad_costupdatematerials

- **表名称：** 单据体-子表
- **表名：** t_cad_costupdatematerials

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatversion | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fmatgrpid | 物料分类编码 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costupdatemats_df |  | fmaterialid,fmatversion,fauxprop |
| 2 | t_cad_costupdatematerials_pkey |  | fentryid |
