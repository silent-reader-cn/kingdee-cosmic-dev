# 方案配置-bdm_scheme_setting

## 方案配置-主表 t_bdm_scheme_setting

- **表名称：** 方案配置-主表
- **表名：** t_bdm_scheme_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fpriority2 | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 4 | fsplitrulecode | 拆分规则编码 | varchar | 50 |  | √ | ' ' | 拆分规则编码 |
| 5 | fmergerule | 合并规则 | int8 | 64 |  | √ | 0 | 合并配置 bdm_merge_rule |
| 6 | fpriority | fpriority | varchar | 7 |  | √ | ' ' |  |
| 7 | fsplitrulename | 拆分规则名称 | varchar | 50 |  | √ | ' ' | 拆分规则名称 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ffilter_tag | 匹配条件_详情 | text | 0 |  |  | null | 匹配条件_详情 |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fstatus | 方案状态 | varchar | 50 |  | √ | ' ' | 方案状态,枚举: 0 :启用 1 :禁用 |
| 12 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: -1 :全部来源 0 :开票申请单 1 :批量导入 |
| 16 | ffilter | 匹配条件 | varchar | 255 |  | √ | ' ' | 匹配条件 |
| 17 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_scheme_setting |  | fid |
| 2 | idx_bdm_scheme_setting |  | forg |
