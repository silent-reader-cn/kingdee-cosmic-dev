# 协同失败数据处理-pbd_scdatahandlefail

## 协同失败数据处理-主表 t_pur_scdatahandlefail

- **表名称：** 协同失败数据处理-主表
- **表名：** t_pur_scdatahandlefail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftraceid | traceid | varchar | 80 |  | √ | ' ' | traceid |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fretry | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 6 | foperatedesc | 实体操作描述 | varchar | 512 |  | √ | ' ' | 实体操作描述 |
| 7 | fparams | 参数集合 | varchar | 255 |  | √ | ' ' | 参数集合 |
| 8 | fresult | 执行结果 | varchar | 255 |  | √ | ' ' | 执行结果 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fresult_tag | 执行结果_详情 | text | 0 |  |  | null | 执行结果_详情 |
| 11 | fusername | 操作用户 | varchar | 255 |  | √ | ' ' | 操作用户 |
| 12 | fstate | 数据处理状态 | varchar | 36 |  | √ | ' ' | 数据处理状态,枚举: normal :队列堆积 success :推送成功 fail :推送失败 intervene :业务干预 |
| 13 | fconfig | 配置集合 | varchar | 255 |  | √ | ' ' | 配置集合 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fparams_tag | 参数集合_详情 | text | 0 |  |  | null | 参数集合_详情 |
| 16 | fconfig_tag | 配置集合_详情 | text | 0 |  |  | null | 配置集合_详情 |
| 17 | fscdatahandleid | 协同数据处理 | varchar | 36 |  | √ | ' ' | 协同数据处理配置 pbd_scdatahandle |
| 18 | fdefinesceneid | 执行场景 | varchar | 36 |  | √ | ' ' | 处理场景定义 pbd_scenedefine |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fentitydesc | 实体描述 | varchar | 255 |  | √ | ' ' | 实体描述 |
| 21 | flogtype | 日志数据类型 | varchar | 36 |  | √ | ' ' | 日志数据类型,枚举: successlog :数据记录 faillog :失败处理 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_sdhf_fcreatetime |  | fcreatetime |
| 2 | idx_t_pur_sdhf_fscdhid |  | fscdatahandleid |
| 3 | pk_t_pur_scdatahandlefail |  | fid |
| 4 | idx_t_pur_sdhf_fstate |  | fstate |
| 5 | idx_t_pur_sdhf_fnumber |  | fnumber |
