# 动态行设置-bdtaxr_template_dynrow

## 单据体-子表 t_bdtaxr_dynrow_checks

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_dynrow_checks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchecklevel | 校验级别 | varchar | 50 |  | √ | ' ' | 校验级别,枚举: A :弱校验 B :强校验 |
| 3 | fcolrange | 列维集合 | varchar | 2000 |  | √ | ' ' | 列维集合 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fdynrowrange | 动态行集合 | varchar | 2000 |  | √ | ' ' | 动态行集合 |
| 7 | fchecktype | 校验类型 | varchar | 50 |  | √ | ' ' | 校验类型,枚举: unique :唯一性校验 |
| 8 | ftitle | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 9 | fcustomservice | 自定义校验器 | varchar | 255 |  | √ | ' ' | 自定义校验器 |
| 10 | fcondition | 前置条件 | varchar | 2000 |  | √ | ' ' | 前置条件 |
| 11 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 12 | fcontent | 提示语 | varchar | 2000 |  | √ | ' ' | 提示语 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_dynrow_checks |  | fentryid |
| 2 | idx_bdtaxr_dynrow_checks_fk |  | fid |

---

## 动态行设置-主表 t_bdtaxr_template_dynrow

- **表名称：** 动态行设置-主表
- **表名：** t_bdtaxr_template_dynrow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 3 | fdisablefrontop | 禁用前端操作 | bpchar | 1 |  | √ | '0' | 禁用前端操作 |
| 4 | fexpanddirection | 扩展方向 | varchar | 50 |  | √ | 'bottom' | 扩展方向,枚举: bottom :向下扩展 right :向右扩展 |
| 5 | fpluginpath | 插件路径 | varchar | 400 |  | √ | ' ' | 插件路径 |
| 6 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: 2 :2.0 3 :3.0 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fidentitycolumn | 标识字段 | varchar | 1000 |  | √ | ' ' | 标识字段,枚举: |
| 9 | frule_name | 规则名称 | varchar | 100 |  | √ | ' ' | 规则名称 |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 11 | fstart_row | 起始行 | varchar | 30 |  | √ | ' ' | 起始行,枚举: 1 :第一行 2 :第二行 |
| 12 | fbusinessidentitycolumn | 业务标识字段 | varchar | 1000 |  | √ | ' ' | 业务标识字段,枚举: |
| 13 | fdynheader | 动态行标题行序号 | int8 | 64 |  | √ | '-1' | 动态行标题行序号 |
| 14 | fzjhzfzszzd | 逐级汇总分组数值字段 | bpchar | 1 |  | √ | '0' | 逐级汇总分组数值字段 |
| 15 | fdynrow_no | 动态行标识 | varchar | 200 |  | √ | ' ' | 动态行标识 |
| 16 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: rule_fetch :规则取数 plugin_fetch :插件取数 |
| 18 | fgroup_no | 动态行组编号 | varchar | 50 |  | √ | ' ' | 动态行组编号 |
| 19 | ftemplate_id | 模版id | int8 | 64 |  | √ | 0 | 模版id |
| 20 | fenable | 是否启用 | varchar | 10 |  | √ | ' ' | 是否启用 |
| 21 | fseq_no | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 22 | ffilter | 启用动态行筛选功能 | bpchar | 1 |  | √ | '0' | 启用动态行筛选功能 |
| 23 | frule_id | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_template_dynrow |  | ftemplate_id |
| 2 | pk_bdtaxr_template_dynrow |  | fid |
