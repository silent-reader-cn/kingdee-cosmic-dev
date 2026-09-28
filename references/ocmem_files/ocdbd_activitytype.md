# 活动类型-ocdbd_activitytype

## 活动类型-多语言表 t_ocdbd_activitytype_l

- **表名称：** 活动类型-多语言表
- **表名：** t_ocdbd_activitytype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_activitytype_l |  | fpkid |
| 2 | idx_ocdbd_atvttypel_flid |  | fid,flocaleid |

---

## 活动类型-主表 t_ocdbd_activitytype

- **表名称：** 活动类型-主表
- **表名：** t_ocdbd_activitytype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fphototype | 拍照方式 | bpchar | 1 |  | √ | 'A' | 拍照方式,枚举: A :必须现场拍照 B :现场或照片库均可 |
| 4 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisneedactivityplan | 必须制定活动方案 | bpchar | 1 |  | √ | '0' | 必须制定活动方案 |
| 8 | factivitysceneid | 活动场景 | int8 | 64 |  | √ | 0 | 活动场景 ocdbd_activityscene |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fismustcostexecution | 必须费用执行 | bpchar | 1 |  | √ | '0' | 必须费用执行 |
| 11 | fpicture | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fismustinputchannel | 必录费用申请渠道 | bpchar | 1 |  | √ | '1' | 必录费用申请渠道 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fkpiid | 关联KPI | int8 | 64 |  | √ | 0 | KPI occbo_kpi_base |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_activitytype_num |  | fnumber |
| 2 | pk_ocdbd_activitytype |  | fid |

---

## 参与角色-多选基础资料表 t_ocdbd_acttype_roles

- **表名称：** 参与角色-多选基础资料表
- **表名：** t_ocdbd_acttype_roles

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 全渠道用户角色 ocdbd_role |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_acttype_roles_fid |  | fid |
| 2 | pk_ocdbd_acttype_roles |  | fpkid |
