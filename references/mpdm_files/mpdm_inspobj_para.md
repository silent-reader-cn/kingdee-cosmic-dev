# 检验对象对接参数表-mpdm_inspobj_para

## 检验对象对接参数表-主表 t_mpdm_inspobjdp

- **表名称：** 检验对象对接参数表-主表
- **表名：** t_mpdm_inspobjdp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fismakepara | 生成参数成功 | bpchar | 1 |  | √ | '0' | 生成参数成功 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | ftgentitynumberid | 触发实体 | varchar | 255 |  | √ | '0' | 主实体对象 bos_entityobject |
| 10 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | ftgopr | 触发操作 | varchar | 50 |  | √ | ' ' | 触发操作,枚举: audit :审核 unaudit :反审核 |
| 12 | fbacktype | 返回类型 | varchar | 5 |  | √ | '' | 返回类型,枚举: 0 :单返 1 :批返 |
| 13 | ftgappid | 触发应用 | varchar | 50 |  | √ | ' ' | 触发应用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_inspdp_fnumber |  | fnumber |
| 2 | idx_mpdm_inspdp_fcreatetime |  | fcreatetime |
| 3 | pk_mpdm_inspobjdp |  | fid |

---

## 单据体-子表 t_mpdm_inspobjdp_e

- **表名称：** 单据体-子表
- **表名：** t_mpdm_inspobjdp_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparainfo | 参数信息 | varchar | 255 |  | √ | ' ' | 参数信息 |
| 3 | fparainfobatch | fparainfobatch | varchar | 255 |  | √ | ' ' |  |
| 4 | fsdentity | 送检实体 | varchar | 50 |  | √ | ' ' | 送检实体 |
| 5 | fbillid | 送检单据ID | varchar | 50 |  | √ | ' ' | 送检单据ID |
| 6 | fparainfo_tag | 参数信息_详情 | text | 0 |  |  | null | 参数信息_详情 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fparainfobatch_tag | fparainfobatch_tag | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_inspobjdp_e |  | fentryid |
| 2 | idx_mpdm_inspdpe_fseq |  | fseq |
| 3 | idx_mpdm_inspdpe_fid |  | fid |

---

## 检验对象对接参数表-多语言表 t_mpdm_inspobjdp_l

- **表名称：** 检验对象对接参数表-多语言表
- **表名：** t_mpdm_inspobjdp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_inspdpl_fid |  | fid,flocaleid |
| 2 | pk_mpdm_inspobjdp_l |  | fpkid |
| 3 | idx_mpdm_inspdpl_fname |  | fname |
