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
| 4 | fscriptcompile_tag | 脚本内容编译_详情 | text | 0 |  |  | null | 脚本内容编译_详情 |
| 5 | fbizunitid | 业务单元id | varchar | 36 |  | √ | ' ' | 业务单元id |
| 6 | fscriptcontext_tag | 脚本内容类型_详情 | text | 0 |  |  | null | 脚本内容类型_详情 |
| 7 | fscriptmodule | 所属模块 | varchar | 50 |  | √ | ' ' | 所属模块 |
| 8 | fscriptcompile | 脚本内容编译 | varchar | 100 |  |  | ' ' | 脚本内容编译 |
| 9 | fclassname | 全路径 | varchar | 200 |  |  | null | 全路径 |
| 10 | fscriptsrcmap | 脚本源码地图 | varchar | 100 |  |  | ' ' | 脚本源码地图 |
| 11 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 13 | fscriptcontext | 脚本内容类型 | varchar | 510 |  |  | null | 脚本内容类型 |
| 14 | fscripttype | 脚本类型 | varchar | 50 |  | √ | ' ' | 脚本类型,枚举: 1 :表单插件 2 :单据插件 3 :列表插件 4 :操作插件 5 :测试用例插件 6 :工具类脚本 10 :转换插件 11 :反写插件 12 :打印插件 13 :导入插件 14 :前端页面脚本 20 :报表表单插件 21 :报表查询扩展插件 22 :报表查询插件 23 :调度执行程序 24 :基础资料个性化控制器 25 :open api插件 26 :单据体导出插件 27 :单据体导入模板插件 28 :单据导入模板插件 29 :工作流插件 |
| 15 | fdescription | 描述 | varchar | 500 |  |  | null | 描述 |
| 16 | finterface | 接口 | varchar | 200 |  | √ | ' ' | 接口 |
| 17 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 应用 |
| 18 | fscriptnumber | 脚本编码 | varchar | 100 |  | √ | ' ' | 脚本编码 |
| 19 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ftype | 表单类型 | varchar | 50 |  | √ | ' ' | 表单类型,枚举: 1 :表单 2 :实体 |
| 21 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 22 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | findustry | 行业 | int8 | 64 |  | √ | 0 | [行业信息 bos_devp_industry](../devportal_files/bos_devp_industry.md) |
| 24 | fscriptsrcmap_tag | 脚本源码地图_详情 | text | 0 |  |  | null | 脚本源码地图_详情 |

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
