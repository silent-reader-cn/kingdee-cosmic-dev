# 业务审批显示设置-mbase_billcfg

## 单据体-子表 t_mbase_bcfgbtnentry

- **表名称：** 单据体-子表
- **表名：** t_mbase_bcfgbtnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtnhide | 隐藏 | bpchar | 1 |  | √ | '0' | 隐藏 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbtnnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbtnname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_bcfgbtnentry |  | fentryid |
| 2 | idx_mbase_bcfgbtnentry_fid |  | fid |

---

## 单据体-子表 t_mbase_billcfgentry

- **表名称：** 单据体-子表
- **表名：** t_mbase_billcfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrylocation | 分录标识 | varchar | 36 |  | √ | ' ' | 分录标识 |
| 3 | fisdefaultshow | 单据头与分录打平时显示分录 | varchar | 1 |  | √ | ' ' | 单据头与分录打平时显示分录 |
| 4 | ffieldname | 字段名称 | varchar | 230 |  | √ | ' ' | 字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentrylocationid | 分录id | varchar | 36 |  | √ | ' ' | 分录id |
| 7 | ffontsize | 字体大小(px) | int8 | 64 |  | √ | 0 | 字体大小(px) |
| 8 | frefparentpropfieldid | 关联的父属性id | varchar | 50 |  | √ | ' ' | 关联的父属性id |
| 9 | fisheadfield | 单据头字段 | varchar | 1 |  | √ | ' ' | 单据头字段 |
| 10 | ffieldid | 字段id | varchar | 36 |  | √ | ' ' | 字段id |
| 11 | feditable | 是否可编辑 | varchar | 1 |  | √ | ' ' | 是否可编辑 |
| 12 | fentrylocationname | 单据体分录名称 | varchar | 230 |  | √ | ' ' | 单据体分录名称 |
| 13 | ffieldkey | 字段标识 | varchar | 36 |  | √ | ' ' | 字段标识 |
| 14 | ffieldpercent | 单据体字段占比(100%,px) | varchar | 10 |  | √ | ' ' | 单据体字段占比(100%,px) |
| 15 | faggregatefunction | 单据体汇总 | varchar | 30 |  | √ | ' ' | 单据体汇总,枚举: Sum :求和 Count :计数 Max :最大 Min :最小 Avg :平均 |
| 16 | ffieldtype | 字段类型 | varchar | 36 |  | √ | ' ' | 字段类型 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | ffontcolor | 字体颜色(#FFFFFF) | varchar | 36 |  | √ | ' ' | 字体颜色(#FFFFFF) |
| 19 | fshowcontent | 显示内容 | varchar | 2000 |  | √ | ' ' | 显示内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bcfgen_fid |  | fid |
| 2 | pk_mbase_billcfgentry |  | fentryid |

---

## 单据体-多语言表 t_mbase_billcfgentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mbase_billcfgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 字段名称 | varchar | 230 |  | √ | ' ' | 字段名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fentrylocationname | 单据体分录名称 | varchar | 230 |  | √ | ' ' | 单据体分录名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_billcfgentry_l |  | fpkid |
| 2 | idx_mbase_bcfgent_l_idloc |  | fentryid,flocaleid |

---

## 单据体-子表 t_mbase_bcfgfieldentry

- **表名称：** 单据体-子表
- **表名：** t_mbase_bcfgfieldentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 3 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 4 | fhide | 隐藏 | bpchar | 1 |  | √ | '0' | 隐藏 |
| 5 | fmodify | 可修改 | bpchar | 1 |  | √ | '0' | 可修改 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ffieldnames | 名称 | varchar | 255 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bcfgfieldentry_fid |  | fid |
| 2 | pk_mbase_bcfgfieldentry |  | fentryid |

---

## 业务审批显示设置-主表 t_mbase_billcfg

- **表名称：** 业务审批显示设置-主表
- **表名：** t_mbase_billcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprocessingmobilepage | 自定义内嵌单据页面 | varchar | 255 |  | √ | ' ' | 自定义内嵌单据页面,枚举: |
| 4 | fstartxtyquickapproval | 启用第三方平台快捷审批 | bpchar | 1 |  | √ | '0' | 启用第三方平台快捷审批 |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flookupdowm | 启用上查下查 | varchar | 1 |  | √ | ' ' | 启用上查下查 |
| 8 | fsonsys | 子系统 | varchar | 230 |  | √ | ' ' | 子系统 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fcardalignment | 内容对齐方式 | varchar | 20 |  | √ | ' ' | 内容对齐方式,枚举: left :左对齐 right :右对齐 center :居中对齐 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | flinenum | 单据体展示行数 | int8 | 64 |  | √ | 0 | 单据体展示行数 |
| 13 | fstyle | 单据体样式 | varchar | 10 |  | √ | ' ' | 单据体样式,枚举: 1 :列表（适用行多列少形式） 2 :卡片（适用行少列多形式） |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsummarytplnum | 单据模板编码 | varchar | 100 |  | √ | ' ' | 单据模板编码 |
| 16 | fstartmobapproval | 是否启用移动审批 | varchar | 1 |  | √ | ' ' | 是否启用移动审批 |
| 17 | ftplname | 摘要模板 | varchar | 100 |  | √ | ' ' | 摘要模板 |
| 18 | fbillno | 单据编号 | varchar | 100 |  |  | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbilltype | 单据名称 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 21 | fpageset | 页面设置选项组 | varchar | 50 |  | √ | '1' | 页面设置选项组,枚举: 1 :generalpage 2 :embedbillpage |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_billcfg |  | fid |
| 2 | idx_mbase_billcfg_billtype |  | fbilltype |
| 3 | dex_mbase_billcfg_mobappr |  | fstartmobapproval |

---

## 业务审批显示设置-多语言表 t_mbase_billcfg_l

- **表名称：** 业务审批显示设置-多语言表
- **表名：** t_mbase_billcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsonsys | 子系统 | varchar | 230 |  | √ | ' ' | 子系统 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_billcfg_l_idloc |  | fid,flocaleid |
| 2 | pk_mbase_billcfg_l |  | fpkid |

---

## 单据体-多语言表 t_mbase_bcfgfieldentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mbase_bcfgfieldentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | ffieldnames | 名称 | varchar | 255 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_bcfgfieldentry_l |  | fpkid |
| 2 | idx_mbase_bcfgfieldentry_l_el |  | fentryid,flocaleid |

---

## 单据体1-子表 t_mbase_billcfgextentry

- **表名称：** 单据体1-子表
- **表名：** t_mbase_billcfgextentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | foperationname | 扩展操作 | varchar | 100 |  | √ | ' ' | 扩展操作 |
| 4 | fbuttonname | 按钮名称 | varchar | 100 |  | √ | ' ' | 按钮名称 |
| 5 | fbuttonnumber | 按钮编码 | varchar | 100 |  | √ | ' ' | 按钮编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bcfgextent_fid |  | fid |
| 2 | pk_mbase_billcfgextentry |  | fentryid |

---

## 单据体-多语言表 t_mbase_bcfgpicentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mbase_bcfgpicentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fliname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bcfgpicentry_l_el |  | fentryid,flocaleid |
| 2 | pk_mbase_bcfgpicentry_l |  | fpkid |

---

## 单据体1-多语言表 t_mbase_billcfgextentry_l

- **表名称：** 单据体1-多语言表
- **表名：** t_mbase_billcfgextentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbuttonname | 按钮名称 | varchar | 100 |  | √ | ' ' | 按钮名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bcfgextent_l_idloc |  | fentryid,flocaleid |
| 2 | pk_mbase_billcfgextentry_l |  | fpkid |

---

## 单据体-子表 t_mbase_bcfgpicentry

- **表名称：** 单据体-子表
- **表名：** t_mbase_bcfgpicentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flivisible | 显示 | bpchar | 1 |  | √ | '0' | 显示 |
| 3 | flinumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fliname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_bcfgpicentry |  | fentryid |
| 2 | idx_mbase_bcfgpicentry_fid |  | fid |

---

## 单据体-多语言表 t_mbase_bcfgbtnentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_mbase_bcfgbtnentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fbtnname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bcfgbtnentry_l_el |  | fentryid,flocaleid |
| 2 | pk_mbase_bcfgbtnentry_l |  | fpkid |
