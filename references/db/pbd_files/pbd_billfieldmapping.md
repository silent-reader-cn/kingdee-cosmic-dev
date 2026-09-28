# 通用映射配置-pbd_billfieldmapping

## 通用映射配置-多语言表 t_pbd_billfieldmapping_l

- **表名称：** 通用映射配置-多语言表
- **表名：** t_pbd_billfieldmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_billfieldmapping_l |  | fid,flocaleid |
| 2 | pk_pbd_billfieldmapping_l |  | fpkid |

---

## 字段映射-子表 t_pbd_billfieldmapping_e

- **表名称：** 字段映射-子表
- **表名：** t_pbd_billfieldmapping_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetobjcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fsourcebillcol | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fispresit | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fformuladesc | 计算公式 | varchar | 512 |  | √ | ' ' | 计算公式 |
| 7 | fselectvalue | 取值 | bpchar | 1 |  | √ | '0' | 取值,枚举: 0 :源单字段 1 :计算公式 2 :按条件取值 |
| 8 | fformula | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |
| 9 | fsourcebillcolno | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 10 | fformula_tag | 计算公式json_详情 | text | 0 |  |  | null | 计算公式json_详情 |
| 11 | ftargetobjcolno | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcandidatekey | 是否候选健 | bpchar | 1 |  | √ | '0' | 是否候选健 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_billfieldmapping_e_fid |  | fid,fseq |
| 2 | pk_pbd_billfieldmapping_e |  | fentryid |

---

## 通用映射配置-主表 t_pbd_billfieldmapping

- **表名称：** 通用映射配置-主表
- **表名：** t_pbd_billfieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fissysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | ftargetobj | 目标业务实体 | varchar | 72 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 11 | fsourcebill | 来源单据 | varchar | 72 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fbizappid | 所属应用 | varchar | 72 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_billfieldmapping |  | fid |
| 2 | idx_pbd_billfieldmapping_fnum |  | fnumber |
