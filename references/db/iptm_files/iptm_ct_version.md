# 上线版本-iptm_ct_version

## 上线版本-主表 t_iptm_ct_version

- **表名称：** 上线版本-主表
- **表名：** t_iptm_ct_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftransferpacketcount | 传输包数量 | int8 | 64 |  | √ | 0 | 传输包数量 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fowner | 负责人 | varchar | 50 |  | √ | ' ' | 负责人 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fenddate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 14 | fonlinearea | 上线领域 | varchar | 50 |  | √ | ' ' | 上线领域 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fversionstatus | 版本状态 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_version |  | fnumber |
| 2 | pk_t_iptm_ct_version |  | fid |

---

## 上线版本-多语言表 t_iptm_ct_version_l

- **表名称：** 上线版本-多语言表
- **表名：** t_iptm_ct_version_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_version_l |  | fid,flocaleid |
| 2 | pk_t_iptm_ct_version_l |  | fpkid |
