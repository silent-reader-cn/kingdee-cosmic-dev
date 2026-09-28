# 通用映射配置-sbs_billfieldmapping

## 字段映射-子表 t_sbs_billfieldmap_e

- **表名称：** 字段映射-子表
- **表名：** t_sbs_billfieldmap_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisentrypreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 3 | ftargetobjcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 4 | fsourcebillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fformuladesc | 计算公式 | varchar | 512 |  | √ | ' ' | 计算公式 |
| 7 | fselectvalue | 取值 | bpchar | 1 |  | √ | '0' | 取值,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 |
| 8 | fformula | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |
| 9 | ftargetobjcolname | ftargetobjcolname | varchar | 255 |  | √ | ' ' |  |
| 10 | fsourcebillcolno | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 11 | fformula_tag | 计算公式json_详情 | text | 0 |  |  | null | 计算公式json_详情 |
| 12 | ftargetobjcolno | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fsourcebillcolname | fsourcebillcolname | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_billfieldmap_e_fid |  | fid |
| 2 | t_sbs_billfieldmap_e_pkey |  | fentryid |

---

## 通用映射配置-多语言表 t_sbs_billfieldmap_l

- **表名称：** 通用映射配置-多语言表
- **表名：** t_sbs_billfieldmap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_bfieldmap_l_id_local |  | fid,flocaleid |
| 2 | t_sbs_billfieldmap_l_pkey |  | fpkid |

---

## 通用映射配置-主表 t_sbs_billfieldmap

- **表名称：** 通用映射配置-主表
- **表名：** t_sbs_billfieldmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 5 | ftargetobj | 目标业务实体 | varchar | 72 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fsourcebill | 来源单据 | varchar | 72 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fbizappid | 所属应用 | varchar | 72 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 12 | fstatus | 单据状态 | varchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_billfieldmap_fnumber |  | fnumber |
| 2 | t_sbs_billfieldmap_pkey |  | fid |
