# 备注设置-bdm_remark

## 备注设置-主表 t_bdm_remark_setting

- **表名称：** 备注设置-主表
- **表名：** t_bdm_remark_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsplittype | 超长后截取方式 | varchar | 50 |  | √ | ' ' | 超长后截取方式,枚举: split_by_field :按字段截取 split_by_length :按长度截取 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | flineremarknamerule | 命名规则 | varchar | 1000 |  | √ | ' ' | 命名规则 |
| 5 | ffilter_tag | 启动条件_详情 | text | 0 |  |  | null | 启动条件_详情 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fremarktype | 备注类型 | varchar | 50 |  | √ | ' ' | 备注类型,枚举: 0 :发票备注 1 :行备注 |
| 9 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | finvoiceremarkseparator | 切换分隔符 | varchar | 50 |  | √ | ' ' | 切换分隔符,枚举: - :- ， :， . :. \ :\ / :/ _ :_ | :| * :* & :& ~ :~ 换行 :换行 |
| 12 | ffilter | 启动条件 | varchar | 255 |  | √ | ' ' | 启动条件 |
| 13 | finvoiceremarknameshow | 命名规则展示 | varchar | 1000 |  | √ | ' ' | 命名规则展示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_remark_setting |  | fid |
| 2 | idx_bdm_remark_setting |  | forg |
