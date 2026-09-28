# 打印字体-bos_prt_font

## 打印字体-主表 t_svc_printfont

- **表名称：** 打印字体-主表
- **表名：** t_svc_printfont

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frcid | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 3 | fname | 字体名称 | varchar | 80 |  | √ | ' ' | 字体名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存 B :提交 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fordernum | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 8 | ftenantid | 租户ID | varchar | 50 |  | √ | ' ' | 租户ID |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :系统预制 2 :自定义 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fnumber | 字体编码 | varchar | 50 |  | √ | ' ' | 字体编码 |
| 14 | falias | falias | varchar | 100 |  | √ | ' ' |  |
| 15 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fisdefault | 默认字体 | bpchar | 1 |  | √ | '0' | 默认字体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_svc_printfont_billno |  | fbillno |
| 2 | pk_svc_printfont_id |  | fid |

---

## 打印字体-多语言表 t_svc_printfont_l

- **表名称：** 打印字体-多语言表
- **表名：** t_svc_printfont_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | falias | 字体名称 | varchar | 100 |  | √ | ' ' | 字体名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_svc_printfont_l |  | fpkid |
| 2 | idx_svc_printfont_l |  | fid,flocaleid |
