# 插件脚本编辑-ide_pluginscript

## 插件脚本编辑-主表 t_meta_pluginscript

- **表名称：** 插件脚本编辑-主表
- **表名：** t_meta_pluginscript

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fenginetype | 引擎类型 | bpchar | 1 |  | √ | '0' | 引擎类型,枚举: 0 :vue 1 :npm |
| 3 | fscriptname | 脚本名称 | varchar | 100 |  | √ | ' ' | 脚本名称 |
| 4 | fbizunitid | 业务单元id | varchar | 36 |  | √ | ' ' | 业务单元id |
| 5 | fscriptcontext_tag | 脚本内容类型_详情 | text | 0 |  |  | null | 脚本内容类型_详情 |
| 6 | fscriptmodule | 所属模块 | varchar | 50 |  | √ | ' ' | 所属模块 |
| 7 | fclassname | 全路径 | varchar | 200 |  |  | null | 全路径 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 10 | fscriptcontext | 脚本内容类型 | varchar | 510 |  |  | null | 脚本内容类型 |
| 11 | fscripttype | 脚本类型 | varchar | 50 |  | √ | ' ' | 脚本类型,枚举: 1 :表单插件 2 :单据插件 3 :列表插件 4 :操作插件 5 :测试用例插件 6 :空白脚本 10 :转换插件 11 :反写插件 12 :打印插件 13 :引入插件 |
| 12 | fdescription | 描述 | varchar | 500 |  |  | null | 描述 |
| 13 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 应用 |
| 14 | fscriptnumber | 脚本编码 | varchar | 100 |  | √ | ' ' | 脚本编码 |
| 15 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 16 | ftype | 表单类型 | varchar | 50 |  | √ | ' ' | 表单类型,枚举: 1 :表单 2 :实体 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | findustry | 行业 | int8 | 64 |  | √ | 0 | 行业信息 bos_devp_industry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_pluginscript_pkey |  | fid |
| 2 | idx_kdp_pluginscript_class |  | fclassname |
| 3 | idx_kdp_pluginscript_name |  | fscriptname |
| 4 | idx_kdp_pluginscript_num |  | fscriptnumber |
