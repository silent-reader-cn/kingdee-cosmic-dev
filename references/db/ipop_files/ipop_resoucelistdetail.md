# 资源清单明细-ipop_resoucelistdetail

## 资源清单明细-主表 t_ipop_resourcelistentity

- **表名称：** 资源清单明细-主表
- **表名：** t_ipop_resourcelistentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 资源基础资料配置 | int8 | 64 |  | √ | 0 | 资源基础资料配置 ipop_resourcebaseconfig |
| 2 | ftag | 标签 | varchar | 255 |  | √ | ' ' | 标签 |
| 3 | fnolimit | 不限量 | varchar | 1 |  | √ | '0' | 不限量 |
| 4 | ftag_tag | 标签_详情 | text | 0 |  |  | null | 标签_详情 |
| 5 | funitid | 显示单位 | int8 | 64 |  | √ | 0 | 资源辅助资料 ipop_resauxiliarydata |
| 6 | fshowinresource | 资源用量中显示 | varchar | 1 |  | √ | '0' | 资源用量中显示 |
| 7 | fbuymore | 显示增购 | varchar | 1 |  | √ | '0' | 显示增购 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fshowusedetail | 显示使用明细 | varchar | 1 |  | √ | '0' | 显示使用明细 |
| 10 | fwarning | 预警提醒 | varchar | 1 |  | √ | '0' | 预警提醒 |
| 11 | fdseq | 显示次序 | int4 | 32 |  | √ | 1 | 显示次序 |
| 12 | fmodulename | 模块名称 | varchar | 50 |  | √ | ' ' | 模块名称 |
| 13 | fsimplecode | 模块简码 | varchar | 50 |  | √ | ' ' | 模块简码 |
| 14 | fthresholdtype | fthresholdtype | varchar | 50 |  | √ | ' ' |  |
| 15 | fclassificationid | 显示栏位 | int8 | 64 |  | √ | 0 | 资源辅助资料 ipop_resauxiliarydata |
| 16 | fspecifications | 默认规格 | numeric | 23 | 10 | √ | 0 | 默认规格 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fmodulenumber | 模块编码 | varchar | 50 |  | √ | ' ' | 模块编码 |
| 19 | fwarningvalue | fwarningvalue | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipop_resourcelistentity |  | fentryid |
| 2 | idx_ipop_resourcelistentity_id |  | fid |
