# 模板库-bos_printtpl_lbr

## 模板库-多语言表 t_svc_printtpl_l

- **表名称：** 模板库-多语言表
- **表名：** t_svc_printtpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fpicture | fpicture | varchar | 256 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 4 | fpic_width | fpic_width | int8 | 64 |  | √ | 0 |  |
| 5 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 6 | fdata | fdata | text | 0 |  |  | null |  |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 8 | fpic_height | fpic_height | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_svc_printtpl_l |  | fid,flocaleid |
| 2 | pk_t_svc_printtpl_l |  | fpkid |

---

## 模板库-主表 t_svc_printtpl

- **表名称：** 模板库-主表
- **表名：** t_svc_printtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 256 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [打印模板库分类 bos_printtpl_lbr_group](../cts_files/bos_printtpl_lbr_group.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmodify_v | 更新版本 | int8 | 64 |  | √ | 0 | 更新版本 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fisv | 开发商标识 | varchar | 50 |  |  | ' ' | 开发商标识 |
| 8 | fpic_height | 图片高度 | int8 | 64 |  | √ | 0 | 图片高度 |
| 9 | fpic_heigh | fpic_heigh | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fpicture | 封面图 | varchar | 256 |  | √ | ' ' | 封面图 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbiztype | 业务类型 | bpchar | 1 |  | √ | '0' | 业务类型,枚举: 0 :常规 1 :蓝牙小票 2 :蓝牙标签 3 :蓝牙针式 |
| 14 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 15 | fcreatorid | 创建人 | varchar | 50 |  | √ | ' ' | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpic_width | 图片宽度 | int8 | 64 |  | √ | 0 | 图片宽度 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdirection | 纸张方向 | bpchar | 1 |  | √ | ' ' | 纸张方向,枚举: A :横向 B :纵向 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fdata | fdata | text | 0 |  |  | null |  |
| 21 | fversion | 版本 | varchar | 30 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_svc_printtpl |  | fid |
| 2 | idx_svc_printtpl_n |  | fnumber |
