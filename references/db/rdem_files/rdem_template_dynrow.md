# 动态行设置-rdem_template_dynrow

## 动态行设置-主表 t_rdem_template_dynrow

- **表名称：** 动态行设置-主表
- **表名：** t_rdem_template_dynrow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdisablefrontop | 禁用前端操作 | bpchar | 1 |  | √ | '0' | 禁用前端操作 |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: 2 :2.0 3 :3.0 |
| 5 | fpluginpath | 插件路径 | varchar | 400 |  | √ | ' ' | 插件路径 |
| 6 | fidentitycolumn | 标识字段 | varchar | 1000 |  | √ | ' ' | 标识字段,枚举: |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | frule_name | 规则名称 | varchar | 50 |  | √ | ' ' | 规则名称 |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 10 | fstart_row | 起始行 | varchar | 50 |  | √ | ' ' | 起始行,枚举: 1 :第一行 2 :第二行 |
| 11 | fdynheader | 动态行标题行序号 | int8 | 64 |  | √ | 0 | 动态行标题行序号 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fdynrow_no | 动态行标识 | varchar | 200 |  | √ | ' ' | 动态行标识 |
| 14 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: rule_fetch :规则取数 plugin_fetch :插件取数 |
| 15 | fgroup_no | 动态行组编号 | varchar | 50 |  | √ | ' ' | 动态行组编号 |
| 16 | ftemplate_id | 模版id | int8 | 64 |  | √ | 0 | 模版id |
| 17 | fenable | 是否启用 | varchar | 50 |  | √ | ' ' | 是否启用 |
| 18 | ffilter | 启用动态行筛选功能 | bpchar | 1 |  | √ | '0' | 启用动态行筛选功能 |
| 19 | fseq_no | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 20 | frule_id | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_template_dynrow |  | fid |

---

## 单据体-子表 t_rdem_dynrow_checks

- **表名称：** 单据体-子表
- **表名：** t_rdem_dynrow_checks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcolrange | 列维集合 | varchar | 2000 |  | √ | ' ' | 列维集合 |
| 3 | fchecklevel | 校验级别 | varchar | 50 |  | √ | ' ' | 校验级别,枚举: A :弱校验 B :强校验 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fdynrowrange | 动态行集合 | varchar | 2000 |  | √ | ' ' | 动态行集合 |
| 7 | fchecktype | 校验类型 | varchar | 50 |  | √ | ' ' | 校验类型,枚举: unique :唯一性校验 |
| 8 | ftitle | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 9 | fcustomservice | 自定义校验器 | varchar | 255 |  | √ | ' ' | 自定义校验器 |
| 10 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 11 | fcondition | 前置条件 | varchar | 2000 |  | √ | ' ' | 前置条件 |
| 12 | fcontent | 提示语 | varchar | 2000 |  | √ | ' ' | 提示语 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_dynrow_checks |  | fentryid |
| 2 | idx_rdem_dynrow_checks_fk |  | fid |
