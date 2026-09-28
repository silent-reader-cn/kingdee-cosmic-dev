# 分片导出配置-fea_exportpageconfig

## 分片导出配置-主表 t_fea_exportpageconfig

- **表名称：** 分片导出配置-主表
- **表名：** t_fea_exportpageconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsinglefile | 独立文件 | bpchar | 1 |  | √ | '0' | 独立文件 |
| 3 | ffiletype | 文件格式 | bpchar | 1 |  | √ | ' ' | 文件格式,枚举: 2 :通用 0 :xml 1 :csv |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fpagesize | 分片大小 | int4 | 32 |  | √ | 0 | 分片大小 |
| 6 | fbizobjid | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fisperiod | 期间相关 | bpchar | 1 |  | √ | '0' | 期间相关 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_exportpageconfig |  | fid |
| 2 | idx_fea_pageconfig_bizobj |  | fbizobjid |
