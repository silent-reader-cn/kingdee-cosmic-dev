# 差异分析方案-cvp_tda_plan

## 差异分析方案-主表 t_cvp_tda_plan

- **表名称：** 差异分析方案-主表
- **表名：** t_cvp_tda_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 255 |  |  | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffield | 文档所属领域 | varchar | 255 |  | √ | 'A' | 文档所属领域,枚举: A :合同文档 B :通用文档 |
| 5 | fdescription | 方案说明 | varchar | 255 |  |  | ' ' | 方案说明 |
| 6 | fmulignore | 忽略项 | varchar | 50 |  |  | '1,2,3' | 忽略项,枚举: 1 :页脚 2 :页眉 3 :目录 |
| 7 | fsupportentity | 区分要素差异和普通差异 | bpchar | 1 |  | √ | '0' | 区分要素差异和普通差异 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmulcatalog | 展示差异分类 | varchar | 50 |  |  | '1,2,3' | 展示差异分类,枚举: 1 :新增 2 :修改 3 :删除 4 :要素差异 5 :普通差异 |
| 10 | fshowlevel2 | 显示二级分类:新增、修改、删除 | bpchar | 1 |  | √ | '0' | 显示二级分类:新增、修改、删除 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fissys | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 14 | fbusinessobject | 使用的业务对象 | varchar | 255 |  |  | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fnumber | 方案编码 | varchar | 255 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_tda_plan_number |  | fnumber |
| 2 | pk_t_cvp_tda_plan |  | fid |
| 3 | idx_cvp_tda_plan_name |  | fname |

---

## 单据体-子表 t_cvp_tdaplan_diffname

- **表名称：** 单据体-子表
- **表名：** t_cvp_tdaplan_diffname

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshowname | 显示名称 | varchar | 8 |  | √ | ' ' | 显示名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdifftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: total :全部 entityDiff :要素差异 commonDiff :普通差异 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_tdaplan_diffname |  | fentryid |
| 2 | idx_t_cvp_tdaplan_diffname_fid |  | fid |
