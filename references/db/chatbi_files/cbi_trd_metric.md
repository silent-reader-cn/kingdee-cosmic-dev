# 第三方指标-cbi_trd_metric

## 第三方指标-主表 t_cbi_trd_metric

- **表名称：** 第三方指标-主表
- **表名：** t_cbi_trd_metric

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 指标模型名称 | varchar | 255 |  | √ | ' ' | 指标模型名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fimplclass | 指标模型定义实现类 | varchar | 400 |  | √ | ' ' | 指标模型定义实现类 |
| 6 | fmetriccontent_tag | 指标模型定义内容_详情 | text | 0 |  |  | null | 指标模型定义内容_详情 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 8 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: announced :已发布 offline :已下线 unannounced :待发布 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmetriccontent | 指标模型定义内容 | text | 0 |  |  | null | 指标模型定义内容 |
| 12 | fcloudid | 所属云 | varchar | 50 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 指标模型编码 | varchar | 255 |  | √ | ' ' | 指标模型编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_trd_metric |  | fid |
| 2 | idx_cbi_trd_metric_number |  | fnumber |
