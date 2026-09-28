# 提取关联设置-cvp_ie_relateconfig

## 信息提取方案名称-多选基础资料表 t_cvp_ie_moulds

- **表名称：** 信息提取方案名称-多选基础资料表
- **表名：** t_cvp_ie_moulds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 信息提取方案 cvp_ie_mouldplan |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_moulds |  | fpkid |
| 2 | idx_t_cvp_ie_moulds |  | fid |

---

## 提取关联设置-主表 t_cvp_ie_relateconfig

- **表名称：** 提取关联设置-主表
- **表名：** t_cvp_ie_relateconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fdescription | 说明 | varchar | 255 |  |  | null | 说明 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | frelateconfig | 关联配置 | text | 0 |  |  | null | 关联配置 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 11 | frelateplannum | 关联方案数 | int8 | 64 |  |  | null | 关联方案数 |
| 12 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 13 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 14 | fbusinessobj | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_relateconfig |  | fid |
| 2 | inx_t_cvp_ie_relateconfig |  | fbillno,fbillstatus |
